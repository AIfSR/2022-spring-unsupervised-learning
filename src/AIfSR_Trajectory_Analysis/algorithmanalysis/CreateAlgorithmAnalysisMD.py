from typing import List, Tuple
from AIfSR_Trajectory_Analysis.algorithms.AlgorithmBase import AlgorithmBase
from AIfSR_Trajectory_Analysis.datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures
from AIfSR_Trajectory_Analysis.datasetfeatures.RealMSDFeatures import RealMSDFeatures
from AIfSR_Trajectory_Analysis.datasets.MacrophageStageDataset import MacrophageStageDataset
from AIfSR_Trajectory_Analysis.datasets.SyntheticDataset import SyntheticDataset
import numpy as np
import pickle
import matplotlib.pyplot as plt
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames
from AIfSR_Trajectory_Analysis.ml_pipelines.MLPipelineBase import MLPipelineBase
from AIfSR_Trajectory_Analysis.normalizefeatures.ScaletoMillion import ScaletoMillion
from AIfSR_Trajectory_Analysis.plotting.FeaturesOverIndices import FeaturesOverIndices
from sklearn.model_selection import train_test_split as split
from sklearn import metrics
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval
import random


def RealPredictions(result: List[Tuple[str, List[float]]], tag:str) -> List[List[float]]:
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


def RealInfo(mlPipeline:MLPipelineBase):
    normalizeFeatures = mlPipeline.getFeatureNormalizer()
    standardizeFeatures = mlPipeline.getFeatureStandardizer()
    algorithm = mlPipeline.getAlgorithm()
    realMSDFeatures = RealMSDFeatures()
    loaded_real_dataset = realMSDFeatures.getDatasetOfFeatures()

    realdataSet = normalizeFeatures.normalizeToSetOfFeatures(loaded_real_dataset)
    realdataSet = standardizeFeatures.standardizeSetOfFeatures(realdataSet)
    real_test_result = algorithm.predict(realdataSet)

    m0_predict = RealPredictions(real_test_result, "M0")
    m1_predict = RealPredictions(real_test_result, "M1")
    m2_predict = RealPredictions(real_test_result, "M2")
    real_predictions = m0_predict + m1_predict + m2_predict

    print()
    print('\033[1m', "Analytics of Predictions: ", '\033[0m')
    print("Here is some percentages and information derived from the predictions of the algorithm")
    print()

    RealAnalytics(m0_predict, "M0")
    RealAnalytics(m1_predict, "M1")
    RealAnalytics(m2_predict, "M2")
    print()
    RealAnalytics(real_predictions, "Ovr")


def displayInaccuracies(Lbls: List[List[float]], result: List[Tuple[str, List[float]]], tag:str, algorithm:AlgorithmBase, dataset:list[FeaturesWithNames]) -> List[str]:
    incorrectResults = []
    print("Incorrectly Labeled trajectories for: " , tag)
    print("Labeling Format:")
    print('\033[1m', "[Ballistic Motion, Confined Diffusion, Random Walk, Very Confinded Diffusion]", '\033[0m')
    print("Line Format:")
    print("Name")
    print("prediction, label")
    print("----------------------------------")
    for label, prediction in zip(Lbls, result):
        predictionName, predictionVal = prediction
        if not label == predictionVal:
            features = getFeaturesByFeaturesName(predictionName, dataset)
            print(predictionName)
            probabilities = algorithm.predictProbabilities([features])[0]
            roundedProb = []
            for prob in probabilities:
                roundedProb.append(round(prob, 2))
            print(roundedProb, ", ", label)
            incorrectResults.append(predictionName)
        
    
    if len(incorrectResults) == 0:
        print("N/A")
    print()
    print()
    
    return incorrectResults

def getFeaturesByFeaturesName(name:str, dataset:list[FeaturesWithNames]) -> FeaturesWithNames:
    for featureWithName in dataset:
        if featureWithName.getName() == name:
            return featureWithName
    print("Could not find: " , name)
    return None

def createIncorGraphs(incorrect_names:list[str], dataSet:list[FeaturesWithNames]):
    print('\033[1m', "Graphs of Incorrect Trajectories:", '\033[0m')
    print("Here is the graphs of the trajectories that were predicted incorrectly")
    plotting = FeaturesOverIndices()
    maxNumberOfGraphs = 8
    if len(incorrect_names) > maxNumberOfGraphs:
        print("There were " + str(len(incorrect_names)) + " total occurances predicted incorrectly. Randomly sampling a " + str(maxNumberOfGraphs) + " number of graphs:")
        incorrect_names = random.sample(incorrect_names, maxNumberOfGraphs)
    for incorrect_name in incorrect_names:
        yFeature = getFeaturesByFeaturesName(incorrect_name, dataSet)
        plotting.display_plot_of_features(yFeatures=yFeature, title=incorrect_name,
                                          yLabel="3DMSD",)

def getRemovedNamesFromPrediction(predictions:list[Tuple[str,List[float]]]) -> list[list[float]]:
    predictionsWithoutNames = []
    for name, prediction in predictions:
        predictionsWithoutNames.append(prediction)
    return predictionsWithoutNames

def createAnalysisDocument(mlPipeline:MLPipelineBase, nameToSaveAlgoAs:str=None):
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
    if(nameToSaveAlgoAs):
        algorithm.save("", nameToSaveAlgoAs)

    test_result = algorithm.predict(testData)
    train_result = algorithm.predict(trnData)
    valid_result = algorithm.predict(valData)
    print(str(mlPipeline), "on dataset:", str(syntheticMSDFeatures))
    
    print('\033[1m', "Accuracy Measurements:", '\033[0m')
    print("Here is the accuracy of our algorithm when the training set, test set,"
        " and cross validation set is passed in")
    print("Accuracy of an algorithm is typically measured based on test set" 
        " accuracy because the algorithm has never seen the \ntest set before")
    print()
    print("Training Accuracy:", metrics.accuracy_score(trnLbls, getRemovedNamesFromPrediction(train_result)))
    print("Test Accuracy:", metrics.accuracy_score(testLbls, getRemovedNamesFromPrediction(test_result)))
    print("Validation Accuracy:", metrics.accuracy_score(valLbls, getRemovedNamesFromPrediction(valid_result)))
    print()
    print()

    print('\033[1m', "Inaccurate Trajectories", '\033[0m')
    print("Here is some more information on the trajectories it predicted incorrectly."
        " It displays the name of the incorrect \ntrajectories, "
        "followed by the incorrect predicted diffusion type and the actual diffusion type.")
    print()
    print()
    names_trn_incor = displayInaccuracies(trnLbls, train_result, "Training Data", algorithm, dataSet)
    names_test_incor = displayInaccuracies(testLbls, test_result, "Testing Data", algorithm, dataSet)
    names_valid_incor = displayInaccuracies(valLbls, valid_result, "CV Data", algorithm, dataSet)
    incorrect_names = names_trn_incor + names_test_incor + names_valid_incor
    # createIncorGraphs(incorrect_names, dataSet)

    # RealInfo(mlPipeline)
