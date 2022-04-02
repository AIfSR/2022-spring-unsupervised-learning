import numpy as np
import pickle
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from normalizefeatures.DoNothingNormalization import DoNothingNormalization
from datasets.SyntheticDatasetSubset import SyntheticDatasetSubset
from datasets.SyntheticDataset import SyntheticDataset
from algorithms.LogisticRegression import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval
from datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures

# Main is the main module that loads in the features of the dataset, trains
# a model on those features and reports the accuracy of that model.
if __name__ == "__main__":
    
    # datasetFeatures defines the dataset and features that will be used for training
    datasetFeatures = SyntheticMSDFeatures()
    # normalizeFeatures defines the way that the features loaded in will be 
    # normalized prior to being input into the algorithm.
    normalizeFeatures = DoNothingNormalization()
    # standardizeFeatures defines the way that the length of the each example's 
    # features will be standardized to ensure that the algorithm can process them
    standardizeFeatures = Extract40ValsRegularInterval()
    # algorithm defines the type of algorithm to be trained
    algorithm = LogisticRegression()

    loadedLabels = datasetFeatures.getLabels()
    loaded_dataSet = datasetFeatures.getDatasetOfFeatures()

    # dataset is normalized and standardized
    dataSet = normalizeFeatures.normalizeToSetOfFeatures(loaded_dataSet)
    dataSet = standardizeFeatures.standardizeSetOfFeatures(dataSet)

    # Sets up the train, test, and cross validation sets
    X_train, X_rem, y_train, y_rem = train_test_split(dataSet, loadedLabels, train_size=0.6, random_state = 1)
    test_size = 0.5
    X_valid, X_test, y_valid, y_test = train_test_split(X_rem, y_rem, test_size=0.5,random_state = 1)

    algorithm.train(X_train, y_train)

    train_prediction = algorithm.predict(X_train)
    test_prediction = algorithm.predict(X_test)
    valid_prediction = algorithm.predict(X_valid)

    yTrain = []
    for i in y_train:
        if i == [1.0, 0.0, 0.0, 0.0]:
            yTrain.append(1)
        elif i == [0.0, 1.0, 0.0, 0.0]:
            yTrain.append(2)
        elif i == [0.0, 0.0, 1.0, 0.0]:
            yTrain.append(3)
        elif i == [0.0, 0.0, 0.0, 1.0]:
            yTrain.append(4)

    yTest = []
    for i in y_test:
        if i == [1.0, 0.0, 0.0, 0.0]:
            yTest.append(1)
        elif i == [0.0, 1.0, 0.0, 0.0]:
            yTest.append(2)
        elif i == [0.0, 0.0, 1.0, 0.0]:
            yTest.append(3)
        elif i == [0.0, 0.0, 0.0, 1.0]:
            yTest.append(4)

    yValid = []
    for i in y_valid:
        if i == [1.0, 0.0, 0.0, 0.0]:
            yValid.append(1)
        elif i == [0.0, 1.0, 0.0, 0.0]:
            yValid.append(2)
        elif i == [0.0, 0.0, 1.0, 0.0]:
            yValid.append(3)
        elif i == [0.0, 0.0, 0.0, 1.0]:
            yValid.append(4)

    print("Training Accuracy:", metrics.accuracy_score(yTrain, train_prediction))
    print("Test Accuracy:", metrics.accuracy_score(yTest, test_prediction))
    print("Validation Accuracy:", metrics.accuracy_score(yValid, valid_prediction))
