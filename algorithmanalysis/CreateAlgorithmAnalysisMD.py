from typing import List
from datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures
from datasetfeatures.MzykMSDFeatures import MzykMSDFeatures
from datasets.MacrophageStageDataset import MacrophageStageDataset
from datasets.SyntheticDataset import SyntheticDataset
import numpy as np
import pickle
import matplotlib.pyplot as plt
from ml_pipelines.MLPipelineBase import MLPipelineBase
from normalizefeatures.ScaletoMillion import ScaletoMillion
from plotting.FeaturesOverIndices import FeaturesOverIndices
from sklearn.model_selection import train_test_split as split
from sklearn import metrics
from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval
realDataset = MacrophageStageDataset()
syntheticDataset = SyntheticDataset()


def getFileNames(indices: List[int]):
    fileNames = []
    for i in indices:
        if 0 <= i <= 1499:
            fileNames.append(syntheticDataset.getCategoriesWithPoints()[0][1][i].title)
        if 1500 <= i <= 2999:
            fileNames.append(syntheticDataset.getCategoriesWithPoints()[1][1][i-1500].title)
        if 3000 <= i <= 4499:
            fileNames.append(syntheticDataset.getCategoriesWithPoints()[2][1][i-3000].title)
        if 4500 <= i <= 5999:
            fileNames.append(syntheticDataset.getCategoriesWithPoints()[3][1][i-4500].title)
    return fileNames


def MyzkPredictions(result: List[List[float]], tag: str) -> List[List[float]]:
    predict = []
    start = 0
    stop = 0
    if tag == "M0":
        start = 0
        stop = 15
    elif tag == "M1":
        start = 15
        stop = 32
    elif tag == "M2":
        start = 32
        stop = 51
    for i in range(start, stop):
        predict.append(result[i])
    return predict


def RealAnalytics(predict: List[List[float]], tag: str) -> None:
    print(tag + ":\tbal: " + str(format((predict.count([1.0, 0.0, 0.0, 0.0]) / len(predict) * 100), '.3f')) +
          "%\tcd: " + str(format((predict.count([0.0, 1.0, 0.0, 0.0]) / len(predict) * 100), '.3f')) +
          "%\trw: " + str(format((predict.count([0.0, 0.0, 1.0, 0.0]) / len(predict) * 100), '.3f')) +
          "%\tvcd: " + str(format((predict.count([0.0, 0.0, 0.0, 1.0]) / len(predict) * 100), '.3f')) + "%")


def MyzkInfo(algorithm):
    normalizeFeatures = ScaletoMillion()
    standardizeFeatures = Extract40ValsRegularInterval()
    realMSDFeatures = MzykMSDFeatures()
    loaded_real_dataset = realMSDFeatures.getDatasetOfFeatures()
    realdataSet = []
    for feature in loaded_real_dataset:
        realdataSet.append(normalizeFeatures.normalizeFeature(feature))
    myzkdataSet = standardizeFeatures.standardizeSetOfFeatures(realdataSet)
    # real_test_result = []
    # for realTrajectory in myzkdataSet:
    #     real_test_result.append(algorithm.predict([realTrajectory]))
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


def displayInaccuracies(Idxs: List[int], Lbls: List[List[float]], result: List[List[float]], tag: str) -> List[int]:
    check_array = []
    for label, prediction in zip(Lbls, result):
        check_array.append(label == prediction)
    incorrect = []
    indices_incorrect = []
    for index, g in enumerate(check_array):
        if not g:
            incorrect.append(index)
    for i in incorrect:
        indices_incorrect.append(Idxs[i])
    if len(incorrect) != 0:
        print("Indexes of incorrect predictions in " + tag + ": ")
        for i in indices_incorrect:
            print(i, end=", ")
        print()
        print("Actual Diffusion Types: ")
        for i in incorrect:
            print(Lbls[i], end=", ")
        print()
        print("Incorrect predictions: ")
        for i in incorrect:
            print(result[i], end=", ")
        print()
        print()
    return indices_incorrect


def createIncorGraphs(total_incorrect, dataSet):
    fileNames = getFileNames(total_incorrect)
    print('\033[1m', "Graphs of Incorrect Trajectories:", '\033[0m')
    print("Here is the graphs of the trajectories that were predicted incorrectly")
    interval = 1198 // 40
    counter = 0
    plotting = FeaturesOverIndices()
    for j in total_incorrect:
        x = []
        for k in range(1, 41):
            x.append(k * interval)
        plotting.display_plot_of_features(xFeatures=x, yFeatures=dataSet[j], title=fileNames[counter],
                                          xLabel="Time Step,s", yLabel="3DMSD",)


def createAnalysisDocument(mlPipeline:MLPipelineBase):
    normalizeFeatures = mlPipeline.getFeatureNormalizer()
    standardizeFeatures = mlPipeline.getFeatureStandardizer()
    algorithm = mlPipeline.getAlgorithm()

    syntheticMSDFeatures = SyntheticMSDFeatures()
    loaded_labels = syntheticMSDFeatures.getLabels()
    loaded_dataSet = syntheticMSDFeatures.getDatasetOfFeatures()
    dataSet = normalizeFeatures.normalizeToSetOfFeatures(loaded_dataSet)
    dataSet = standardizeFeatures.standardizeSetOfFeatures(dataSet)
    indices = np.arange(len(dataSet))
    (trnData, remData, trnLbls, remLbls, trnIdxs, remIdxs)\
        = split(dataSet, loaded_labels, indices, train_size=0.6, random_state=1)

    (testData, valData, testLbls, valLbls, testIdxs, valIdxs) \
        = split(remData, remLbls, remIdxs, test_size=0.5, random_state=2)

    algorithm.train(trnData, trnLbls)
    test_result = algorithm.predict(testData)
    train_result = algorithm.predict(trnData)
    valid_result = algorithm.predict(valData)

    print('\033[1m', "Accuracy Measurements:", '\033[0m')
    print("Here is the accuracy of our algorithm when the training set, test set,"
          " and cross validation set is passed in")
    print()
    print("Training Accuracy:", metrics.accuracy_score(trnLbls, train_result))
    print("Test Accuracy:", metrics.accuracy_score(testLbls, test_result))
    print("Validation Accuracy:", metrics.accuracy_score(valLbls, valid_result))
    print()
    print()

    print('\033[1m', "Inaccurate Trajectories", '\033[0m')
    print("Here is some more information on the trajectories it predicted incorrectly."
          " It displays the indexes of the incorrect trajectories, "
          "followed by the actual diffusion type and the incorrect predicted diffusion type.")
    print()
    print('\033[1m', "[Ballistic Motion,Confined Diffusion,Random Walk,Very Confinded Diffusion]", '\033[0m')
    print()
    idxs_trn_incor = displayInaccuracies(trnIdxs, trnLbls, train_result, "training")
    idxs_test_incor = displayInaccuracies(testIdxs, testLbls, test_result, "testing")
    idxs_valid_incor = displayInaccuracies(valIdxs, valLbls, valid_result, "validation")

    total_incorrect = idxs_trn_incor + idxs_test_incor + idxs_valid_incor
    createIncorGraphs(total_incorrect, dataSet)
    print(type(dataSet[1]))

    MyzkInfo(algorithm)
