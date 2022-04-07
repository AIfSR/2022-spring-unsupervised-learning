from typing import List, Tuple
from datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures
from datasetfeatures.MzykMSDFeatures import MzykMSDFeatures
from datasets.MacrophageStageDataset import MacrophageStageDataset
from datasets.SyntheticDataset import SyntheticDataset
import numpy as np
import pickle
import matplotlib.pyplot as plt
from features.FeaturesWithNames import FeaturesWithNames
from ml_pipelines.MLPipelineBase import MLPipelineBase
from normalizefeatures.ScaletoMillion import ScaletoMillion
from plotting.FeaturesOverIndices import FeaturesOverIndices
from sklearn.model_selection import train_test_split as split
from sklearn import metrics
from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval


def MyzkPredictions(result: List[Tuple[str, List[float]]], tag:str) -> List[List[float]]:
    predict = []
    for name, prediction in result:
        if tag in name:
            predict.append(prediction)
    return predict

def RealAnalytics(predict: List[List[float]], tag: str) -> None:
    print(tag + ":\tbal: " + str(format((predict.count([1.0, 0.0, 0.0, 0.0]) / len(predict) * 100), '.3f')) +
          "%\tcd: " + str(format((predict.count([0.0, 1.0, 0.0, 0.0]) / len(predict) * 100), '.3f')) +
          "%\trw: " + str(format((predict.count([0.0, 0.0, 1.0, 0.0]) / len(predict) * 100), '.3f')) +
          "%\tvcd: " + str(format((predict.count([0.0, 0.0, 0.0, 1.0]) / len(predict) * 100), '.3f')) + "%")


def MyzkInfo(mlPipeline:MLPipelineBase):
    normalizeFeatures = mlPipeline.getFeatureNormalizer()
    standardizeFeatures = mlPipeline.getFeatureStandardizer()
    algorithm = mlPipeline.getAlgorithm()
    realMSDFeatures = MzykMSDFeatures()
    loaded_real_dataset = realMSDFeatures.getDatasetOfFeatures()

    realdataSet = []
    for feature in loaded_real_dataset:
        realdataSet.append(normalizeFeatures.normalizeFeature(feature))
    myzkdataSet = standardizeFeatures.standardizeSetOfFeatures(realdataSet)
    real_test_result = algorithm.predict(myzkdataSet)

    m0_predict = MyzkPredictions(real_test_result, "M0")
    m1_predict = MyzkPredictions(real_test_result, "M1")
    m2_predict = MyzkPredictions(real_test_result, "M2")
    myzk_predictions = m0_predict + m1_predict + m2_predict

    print()
    print('\033[1m', "Analytics of Predictions: ", '\033[0m')
    print("Here is some percentages and information derived from the predictions of the algorithm")
    print()

    RealAnalytics(m0_predict, "M0")
    RealAnalytics(m1_predict, "M1")
    RealAnalytics(m2_predict, "M2")
    RealAnalytics(myzk_predictions, "Ovr")


def displayInaccuracies(Lbls: List[List[float]], result: List[Tuple[str, List[float]]], tag:str) -> List[str]:
    incorrectResults = []
    names = ""
    incorrectPredictions = ""
    actualDiffusionTypes = ""
    for label, prediction in zip(Lbls, result):
        predictionName, predictionVal = prediction
        if not label == predictionVal:
            incorrectResults.append(predictionName)
            names += predictionName + "\n"
            incorrectPredictions += str(predictionVal) + "\n"
            actualDiffusionTypes += str(label) + "\n"
    
    if len(incorrectResults) != 0:
        print("Names of incorrect predictions for: " + tag)
        print(names)
        print("Actual Diffusion Types: ")
        print(actualDiffusionTypes)
        print("Incorrect predictions: ")
        print(incorrectPredictions)  
    else:
        print("Algorithm correctly predicted all labels for: " + tag)
    print()
    print()
    
    return incorrectResults

def getFeaturesByFeaturesName(name:str, dataset:list[FeaturesWithNames]) -> FeaturesWithNames:
    for featureWithName in dataset:
        if featureWithName.getName() == name:
            return featureWithName
    print("Could not find: " , name)
    return None

def createIncorGraphs(incorrect_names, dataSet):
    print('\033[1m', "Graphs of Incorrect Trajectories:", '\033[0m')
    print("Here is the graphs of the trajectories that were predicted incorrectly")
    plotting = FeaturesOverIndices()
    for incorrect_name in incorrect_names:
        yFeature = getFeaturesByFeaturesName(incorrect_name, dataSet)
        plotting.display_plot_of_features(yFeatures=yFeature, title=incorrect_name,
                                          yLabel="3DMSD",)

def getRemovedNamesFromPrediction(predictions:list[Tuple[str,List[float]]]) -> list[list[float]]:
    predictionsWithoutNames = []
    for name, prediction in predictions:
        predictionsWithoutNames.append(prediction)
    return predictionsWithoutNames

def createAnalysisDocument(mlPipeline:MLPipelineBase):
    normalizeFeatures = mlPipeline.getFeatureNormalizer()
    standardizeFeatures = mlPipeline.getFeatureStandardizer()
    algorithm = mlPipeline.getAlgorithm()

    syntheticMSDFeatures = SyntheticMSDFeatures()
    loaded_labels = syntheticMSDFeatures.getLabels()
    loaded_dataSet = syntheticMSDFeatures.getDatasetOfFeatures()
    dataSet = normalizeFeatures.normalizeToSetOfFeatures(loaded_dataSet)
    dataSet = standardizeFeatures.standardizeSetOfFeatures(dataSet)
    (trnData, remData, trnLbls, remLbls)\
        = split(dataSet, loaded_labels, train_size=0.6, random_state=1)

    (testData, valData, testLbls, valLbls) \
        = split(remData, remLbls, test_size=0.5, random_state=2)

    algorithm.train(trnData, trnLbls)
    test_result = algorithm.predict(testData)
    train_result = algorithm.predict(trnData)
    valid_result = algorithm.predict(valData)

    print('\033[1m', "Accuracy Measurements:", '\033[0m')
    print("Here is the accuracy of our algorithm when the training set, test set,"
          " and cross validation set is passed in")
    print()
    print("Training Accuracy:", metrics.accuracy_score(trnLbls, getRemovedNamesFromPrediction(train_result)))
    print("Test Accuracy:", metrics.accuracy_score(testLbls, getRemovedNamesFromPrediction(test_result)))
    print("Validation Accuracy:", metrics.accuracy_score(valLbls, getRemovedNamesFromPrediction(valid_result)))
    print()
    print()

    print('\033[1m', "Inaccurate Trajectories", '\033[0m')
    print("Here is some more information on the trajectories it predicted incorrectly."
          " It displays the name of the incorrect trajectories, "
          "followed by the actual diffusion type and the incorrect predicted diffusion type.")
    print()
    print('\033[1m', "[Ballistic Motion,Confined Diffusion,Random Walk,Very Confinded Diffusion]", '\033[0m')
    print()
    names_trn_incor = displayInaccuracies(trnLbls, train_result, "Training Data")
    names_test_incor = displayInaccuracies(testLbls, test_result, "Testing Data")
    names_valid_incor = displayInaccuracies(valLbls, valid_result, "CV Data")
    incorrect_names = names_trn_incor + names_test_incor + names_valid_incor
    createIncorGraphs(incorrect_names, dataSet)

    MyzkInfo(mlPipeline)