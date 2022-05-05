from typing import Tuple

import AIfSR_Trajectory_Analysis.PredictDiffusionTypes as PredictDiffusionTypes
from AIfSR_Trajectory_Analysis.datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures
from AIfSR_Trajectory_Analysis.features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from AIfSR_Trajectory_Analysis.features.FeatureCreatorBase import FeatureCreatorBase
from AIfSR_Trajectory_Analysis.datasets.SyntheticDataset import SyntheticDataset
from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames
from AIfSR_Trajectory_Analysis.normalizefeatures.DivideByMaxNormalization import DivideByMaxNormalization
from AIfSR_Trajectory_Analysis.plotting.FeaturesOverIndices import FeaturesOverIndices
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.ExtractValsRegularInterval import ExtractValsRegularInterval
from AIfSR_Trajectory_Analysis.algorithms.LogisticRegression import LogisticRegression
from sklearn.model_selection import train_test_split as split
from sklearn import metrics
import time

def predict(inputTrajectoriesDirectory:str, locationOfXlsx:str = None, sheetName:str = None):
    """This is the function used to predict the diffusion types of trajectories 
    using the most accurate machine learning model within this build. Pass in 
    the path to a directory as a string and every trajectory within that 
    directory will be analyzed. Trajectories are files that end in .tck and 
    contain x,y,z,t points in the following format:
    line 1: x points, seperated by spaces
    line 2: y points, seperated by spaces
    line 3: z points, seperated by spaces
    line 4: t points, seperated by spaces
    
    If you would like to export the results to an excel spreadsheet, pass in the 
    location of the excel spreadsheet you would like to export to into the 
    parameter locationOfXlsx. You can further specify the name of the sheet that 
    will be made within the spreadsheet by passing a string into the sheet 
    parameter. If no sheet name is provided, today's date will be used as the 
    sheet name 

    If no name of a spreadsheet is passed in then this function will print out 
    the file names of the trajectories it predicts and then the type(s) of 
    diffusion that it detects within those trajectories.

    Example usage (Assume /Users/seandoyle/MyDirectory is a directory containing 
    the trajectories: Trajectory1.tck, Trajectory2.tck, and Trajectory3.tck):
    >>> predict("/Users/seandoyle/MyDirectory")
    /Users/seandoyle/MyDirectory/Trajectory1.tck:
    Ballistic: No, Confined Diffusion: No, Random Walk: Yes, Very Confined Diffusion: No

    /Users/seandoyle/MyDirectory/Trajectory2.tck:
    Ballistic: No, Confined Diffusion: No, Random Walk: No, Very Confined Diffusion: Yes

    /Users/seandoyle/MyDirectory/Trajectory3.tck:
    Ballistic: No, Confined Diffusion: Yes, Random Walk: No, Very Confined Diffusion: No
    """
    PredictDiffusionTypes.checkDirectory(inputTrajectoriesDirectory)
    if locationOfXlsx:
        PredictDiffusionTypes.checkOutputToXlsxFile(locationOfXlsx)
    mlPipeline = PredictDiffusionTypes.MultiLRPipelineFactory()

    algorithm = mlPipeline.getAlgorithm()
    
    points = PredictDiffusionTypes.getTrajectories(inputTrajectoriesDirectory)
    inputFeatures = PredictDiffusionTypes.getFeaturesForAlgorithm(points, mlPipeline)

    predictions = algorithm.predict_prob(inputFeatures)
    labels = ["Ballistic Motion","Confined Diffusion","Random Walk","Very Confinded Diffusion"]
    if locationOfXlsx:
        PredictDiffusionTypes.outputToXlsxFile(predictions, labels, locationOfXlsx, sheetName)
    else:
        PredictDiffusionTypes.printPredictions(predictions, labels)


    

        

    PredictDiffusionTypes.printPredictions(predictions)
