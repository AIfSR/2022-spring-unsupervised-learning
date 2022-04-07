import numpy as np
import sys
import os
from algorithms.LogisticRegression import LogisticRegression
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from normalizefeatures.ScaletoMillion import ScaletoMillion
from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval
from tckfilereader.TCKFileReader import TCKFileReader

# Main is the main module that loads in the features of the dataset, trains
# a model on those features and reports the accuracy of that model.
if __name__ == "__main__":
    
    featureCreator = ThreeDMSDFeatureCreator()
    # normalizeFeatures defines the way that the features loaded in will be 
    # normalized prior to being input into the algorithm.
    normalizeFeatures = ScaletoMillion()
    # standardizeFeatures defines the way that the length of the each example's 
    # features will be standardized to ensure that the algorithm can process them
    standardizeFeatures = Extract40ValsRegularInterval()
    # algorithm defines the type of algorithm to be trained
    algorithm = LogisticRegression()

    algorithm.load("algorithms/LR_V1.0.pkl")
    inputTrajectoriesDirectory = sys.argv[1]
    inputPoints = []
    tckFileReader = TCKFileReader()

    for filename in os.listdir(inputTrajectoriesDirectory):
        f = os.path.join(inputTrajectoriesDirectory, filename)
        # checking if it is a file
        if not os.path.isfile(f):
            continue
        inputPoints.append(tckFileReader.get_points_with_name(f, False))
    
    inputFeatures = []
    for points in inputPoints:
        features = featureCreator.get_features(points)
        features = normalizeFeatures.normalizeFeature(features)
        features = standardizeFeatures.standardizeFeatures(features)
        inputFeatures.append(features)

    predictions = algorithm.predict(inputFeatures)

    for prediction, pointsWithNames in zip(predictions, inputPoints):
        print(pointsWithNames.getName() + ": " + str(prediction))
    
