from typing import Tuple
import numpy as np
import sys
import os
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.ml_pipelines.MultiLRPipelineFactory import MultiLRPipelineFactory
from AIfSR_Trajectory_Analysis.ml_pipelines.MLPipelineBase import MLPipelineBase
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.FeatureStandardizationError import FeatureStandardizationError
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames
from AIfSR_Trajectory_Analysis.tckfilereader.TCKFileReader import TCKFileReader

def checkDirectory(directory:str) -> None:
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

def printPredictions(predictions:list[Tuple[str, list[float]]]) -> None:
    for name, prediction in predictions:
        output = name + ": \n"
        if prediction == [1.0, 0.0, 0.0]:
            output += "Ballistic: Yes, Confined Diffusion: No, Random Walk: No"
        elif prediction == [0.0, 1.0, 0.0]:
            output += "Ballistic: No, Confined Diffusion: Yes, Random Walk: No"
        elif prediction == [0.0, 0.0, 1.0]:
            output += "Ballistic: No, Confined Diffusion: No, Random Walk: Yes"
        else:
            output += str(prediction)
        output += "\n"
        print(output)
