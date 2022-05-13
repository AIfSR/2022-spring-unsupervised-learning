from typing import List, Tuple
from AIfSR_Trajectory_Analysis.datasetfeatures.MultiLabelSyntheticMSDFeatures import MultiLabelSyntheticMSDFeatures
from AIfSR_Trajectory_Analysis.datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures
from AIfSR_Trajectory_Analysis.ml_pipelines.MultiLRPipelineFactory import MultiLRPipelineFactory
from AIfSR_Trajectory_Analysis.ml_pipelines.OvRLRPipelineFactory import OvRLRPipelineFactory
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
import random

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


def createIncorGraphs(incorrect_names:list[str], dataSet:list[FeaturesWithNames]):
    print('\033[1m', "Graphs of Incorrect Trajectories:", '\033[0m')
    print("Here is the graphs of the trajectories that were predicted incorrectly")
    plotting = FeaturesOverIndices()
    maxNumberOfGraphs = 8
    if len(incorrect_names) > maxNumberOfGraphs:
        print("There were " + str(len(incorrect_names)) + " total occurances predicted incorrectly. "
                                                          "Randomly sampling a " + str(maxNumberOfGraphs)
                                                          + " number of graphs:")
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


def removeConfinementEscape(dataset, labels):
    newDataset = []
    newLabels = []
    for feature, label in zip(dataset, labels):
        if "Confinement_escape" not in feature.getName():
            newDataset.append(feature)
            newLabels.append(label)
    print("# of Confinement_escape removed: " + str(len(dataset) - len(newDataset)))
    return newDataset, newLabels


def createAnalysisDocument(mlPipeline:MLPipelineBase, nameToSaveAlgoAs: str = None):
    normalizeFeatures = mlPipeline.getFeatureNormalizer()
    standardizeFeatures = mlPipeline.getFeatureStandardizer()
    algorithm = mlPipeline.getAlgorithm()

    syntheticMSDFeatures = SyntheticMSDFeatures()
    MultisyntheticMSDFeatures = MultiLabelSyntheticMSDFeatures()

    if isinstance(mlPipeline, MultiLRPipelineFactory):
        loaded_labels = syntheticMSDFeatures.getLabels()
        loaded_dataSet = syntheticMSDFeatures.getDatasetOfFeatures()
    elif isinstance(mlPipeline, OvRLRPipelineFactory):
        loaded_labels = syntheticMSDFeatures.getLabels() + MultisyntheticMSDFeatures.getLabels()
        loaded_dataSet = syntheticMSDFeatures.getDatasetOfFeatures() + MultisyntheticMSDFeatures.getDatasetOfFeatures()

    loaded_dataSet, loaded_labels = removeConfinementEscape(loaded_dataSet, loaded_labels)

    dataSet = normalizeFeatures.normalizeToSetOfFeatures(loaded_dataSet)
    dataSet = standardizeFeatures.standardizeSetOfFeatures(dataSet)
    print("Number of features per trajectory:" , len(dataSet[0]))
    (trnData, remData, trnLbls, remLbls)\
        = split(dataSet, loaded_labels, train_size=0.6, random_state=1)

    (valData, testData, valLbls, testLbls) \
        = split(remData, remLbls, test_size=0.5, random_state=2)

    algorithm.train(trnData, trnLbls)
    if(nameToSaveAlgoAs):
        algorithm.save("", nameToSaveAlgoAs)

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

