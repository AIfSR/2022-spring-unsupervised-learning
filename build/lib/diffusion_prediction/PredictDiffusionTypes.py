import numpy as np
import sys
import os
from diffusion_prediction.features.Features import Features
from diffusion_prediction.ml_pipelines.LRPipelineFactory import LRPipelineFactory
from diffusion_prediction.ml_pipelines.MLPipelineBase import MLPipelineBase
from diffusion_prediction.standardizefeaturesnumber.FeatureStandardizationError import FeatureStandardizationError
from diffusion_prediction.tckfilereader.Points import Points
from diffusion_prediction.tckfilereader.PointsWithNames import PointsWithNames
from diffusion_prediction.tckfilereader.TCKFileReader import TCKFileReader

def checkDirectory(directory:str) -> None:
    directory = sys.argv[1]
    if(not os.path.isdir(directory)):
        raise IOError("Cannot find directory: " + directory)

def checkFileIsValid(fileName:str) -> bool:
    """Checks to ensure that a string is a valid file path and that it is a tck 
    file"""
    if not os.path.isfile(fileName):
        return False
    if not fileName.split(".")[-1] == "tck":
        return False
    return True

def getTrajectories(inputTrajectoriesDirectory:str) -> list[Points]:
    """Gets all of the trajectories as Points objects found within the 
    inputTrajectoriesDirectory directory"""
    points = []
    tckFileReader = TCKFileReader()
    for filename in os.listdir(inputTrajectoriesDirectory):
        f = os.path.join(inputTrajectoriesDirectory, filename)
        if(not checkFileIsValid(f)):
            print("Could not read file: ", f)
            continue
        points.append(tckFileReader.get_points_with_name(f, False))
    if len(points) == 0:
        raise IOError("Could not read any files in: " + inputTrajectoriesDirectory)
    return points

def getFeaturesForAlgorithm(trajectories:list[PointsWithNames], mlPipeline:MLPipelineBase) -> list[Features]:
    # The featureCreator converts points of a trajectory to features
    featureCreator = mlPipeline.getFeatureCreator()
    # The normalizeFeatures normalizes the feature values to ensure that feature 
    # values passed into an algorithm are in an acceptable range.
    normalizeFeatures = mlPipeline.getFeatureNormalizer()
    # The standardizeFeatures standardized the number of features that the 
    # algorithm takes to ensure that each occurance has a set number of features
    standardizeFeatures = mlPipeline.getFeatureStandardizer()

    allFeatures = []
    for trajectory in trajectories:
        try:
            features = featureCreator.get_features(trajectory)
            features = normalizeFeatures.normalizeFeature(features)
            features = standardizeFeatures.standardizeFeatures(features)
            allFeatures.append(features)
        except:
            print("Could not process file: ")
            print(trajectory.getName())
            print("Does this trajectory have enough points? (more than 50 x,y,z,t points)")
            print()
        
    return allFeatures

# predict is the main method that reads in the trajectories, calculates the MSD 
# values for them, predicts their diffusion types, and then prints out these 
# predictions
def predict(inputTrajectoriesDirectory:str):

    # This is the concrete factory class that defines the feature creator, 
    # normalizer, standardizer, and algorithm being used to process the 
    # trajectories for the Logistic Regression algorithm

    checkDirectory(inputTrajectoriesDirectory)

    mlPipeline = LRPipelineFactory()

    algorithm = mlPipeline.getAlgorithm()
    
    points = getTrajectories(inputTrajectoriesDirectory)
    inputFeatures = getFeaturesForAlgorithm(points, mlPipeline)

    predictions = algorithm.predict(inputFeatures)

    for name, prediction in predictions:
        print(name + ": " + str(prediction))
    
