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
    mlPipeline = PredictDiffusionTypes.LRPipelineFactory()

    algorithm = mlPipeline.getAlgorithm()
    
    points = PredictDiffusionTypes.getTrajectories(inputTrajectoriesDirectory)
    inputFeatures = PredictDiffusionTypes.getFeaturesForAlgorithm(points, mlPipeline)

    predictions = algorithm.predict_prob(inputFeatures)
    labels = ["Ballistic Motion","Confined Diffusion","Random Walk","Very Confinded Diffusion"]
    if locationOfXlsx:
        PredictDiffusionTypes.outputToXlsxFile(predictions, labels, locationOfXlsx, sheetName)
    else:
        PredictDiffusionTypes.printPredictions(predictions, labels)

def quick_train(featureCreators:list[Tuple[FeatureCreatorBase,int]], trajectoriesPerCategory:int=200, graphsPerCategory:int=3):
    """ This code trains a machine learning algorithm are the features passed in, 
    outputs the results of the algorithm, and also displays a few graphs of the 
    features that the algorithm was trained and evaluated on.

    :param list[Tuple[FeatureCreatorBase,int]] featureCreators: This is a list
    of the types of features, and the number of features to extract from each
    trajectory. Each FeatureCreatorBase will extract a large number of features
    from each trajectory. The integer included in the tuple is used to scale
    down this number so as not to overwhelm the algorithm

    :param int trajectoriesPerCategory: specifies the number of trajectories 
    that will be analyzed per category(the categories being the four different 
    types of diffusion types: Ballistic, Confined Diffusion, Random Walk, and 
    Very Confined Diffusion)

    :param int graphsPerCategory: specifies the number of graphs for each label
    category that will be displayed
    
    """
    def getRemovedNamesFromPrediction(predictions:list[Tuple[str,list[float]]]) -> list[list[float]]:
        predictionsWithoutNames = []
        for name, prediction in predictions:
            predictionsWithoutNames.append(prediction)
        return predictionsWithoutNames

    def getMSDFeaturesByFeaturesName(name:str) -> FeaturesWithNames:
        for featureWithName in msdDataset:
            if featureWithName.getName() == name:
                return featureWithName
        print("Could not find: " , name)
        return None
    
    print("Loading trajectories")

    msdDataset = SyntheticMSDFeatures().getDatasetOfFeatures()
    categories = SyntheticDataset().getCategoriesWithPoints(trajectoriesPerCategory)
    print()

    featureNormalizer = DivideByMaxNormalization()
    featureStandardizer = ExtractValsRegularInterval()
    algorithm = LogisticRegression()
    features = []
    labels = []
    featuresToGraph = []
    print("Extracting Features:")

    totalTrajectories = 0
    for _, trajectories in categories:
        totalTrajectories += len(trajectories)
    count = 0
    for tag, trajectories in categories:
        numberOfFeaturesInTagToGraph = 0
        for trajectory in trajectories:
            if(count % (totalTrajectories // 5) == 0):
                print(str(count), "/" , str(totalTrajectories), " trajectory's features extracted")
            
            feature = trajectory.getFeaturesToInitialize()
            for featureCreator, number in featureCreators:
                if(number <= 0):
                    continue
                if type(featureCreator) == ThreeDMSDFeatureCreator:
                    newFeatures = getMSDFeaturesByFeaturesName(feature.getName())
                else:
                    newFeatures = featureCreator.get_features(trajectory)
                newFeatures = featureNormalizer.normalizeFeature(newFeatures)
                newFeatures = featureStandardizer.standardizeFeatures(newFeatures, number)
                feature += newFeatures
            features.append(feature)
            if tag == "Bal":
                labels.append([1.0, 0.0, 0.0, 0.0])
            elif tag == "CD":
                labels.append([0.0, 1.0, 0.0, 0.0])
            elif tag == "RW":
                labels.append([0.0, 0.0, 1.0, 0.0])
            elif tag == "VCD":
                labels.append([0.0, 0.0, 0.0, 1.0])
            else:
                print("Unidentified tag: " , tag)
                assert(False)

            if(numberOfFeaturesInTagToGraph < graphsPerCategory):
                featuresToGraph.append(feature)
                numberOfFeaturesInTagToGraph += 1
            count += 1
    print()

    (trnData, testData, trnLbls, testLbls)\
        = split(features, labels, train_size=0.8, random_state=1)
    print("Training Algorithm on ", str(len(trnData)), " trajectories")
    algorithm.train(trnData, trnLbls)
    train_result = algorithm.predict(trnData)

    print("Training Accuracy:", metrics.accuracy_score(trnLbls, getRemovedNamesFromPrediction(train_result)))
    test_result = algorithm.predict(testData)
    print("Testing Algorithm on ", str(len(testData)), " trajectories")
    print("Test Accuracy: ", metrics.accuracy_score(testLbls, getRemovedNamesFromPrediction(test_result)))

    print()
    print("Here are a few graphs of the features generated:")

    plotting = FeaturesOverIndices()
    for feature in featuresToGraph:
        plotting.display_plot_of_features(yFeatures=feature, title=feature.getName(),
                                          yLabel="Trajectory Features", yRange=(1.0e-6, 1.0))


    

        
