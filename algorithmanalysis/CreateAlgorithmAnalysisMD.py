from typing import List
from datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures
from datasets.MacrophageStageDataset import MacrophageStageDataset
from datasets.SyntheticDataset import SyntheticDataset
import numpy as np
import pickle
import matplotlib.pyplot as plt
from normalizefeatures.DoNothingNormalization import DoNothingNormalization
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


def convert2dLabelsTo1d(twoDLabels: list[list[float]]) -> list[float]:
    oneDLabels = []
    for i in twoDLabels:
        if i == [1.0, 0.0, 0.0, 0.0]:
            oneDLabels.append(1)
        elif i == [0.0, 1.0, 0.0, 0.0]:
            oneDLabels.append(2)
        elif i == [0.0, 0.0, 1.0, 0.0]:
            oneDLabels.append(3)
        elif i == [0.0, 0.0, 0.0, 1.0]:
            oneDLabels.append(4)
    return oneDLabels


def MyzkPredictions(algorithm):
    normalizeFeatures = DoNothingNormalization()
    standardizeFeatures = Extract40ValsRegularInterval()
    myzkdataFile = open("Mzykdata.pkl", "rb")
    loaded_mzyk_dataSet = pickle.load(myzkdataFile)
    myzkdataFile.close()
    mzykdataSet = normalizeFeatures.normalizeToSetOfFeatures(loaded_mzyk_dataSet)
    myzkdataSet = standardizeFeatures.standardizeSetOfFeatures(mzykdataSet)
    mzyk_test_result = algorithm.predict(myzkdataSet)

    print('\033[1m', "Predictions of Dr. Mzyk's Data:", '\033[0m')
    print("Here is the predictions of our algorithm when Dr. Mzyk's data is passed in")
    print()
    m0_predict = []
    m1_predict = []
    m2_predict = []
    print("M0: ", end="")
    for i in range(0, 15):
        print(mzyk_test_result[i], end=", ")
        m0_predict.append(mzyk_test_result[i])
    print()
    print("M1: ", end="")
    for i in range(15, 32):
        print(mzyk_test_result[i], end=", ")
        m1_predict.append(mzyk_test_result[i])
    print()
    print("M2: ", end="")
    for i in range(32, 51):
        print(mzyk_test_result[i], end=", ")
        m2_predict.append(mzyk_test_result[i])
    myzk_predictions = m0_predict + m1_predict + m2_predict
    print()
    print()
    print('\033[1m', "Analytics of Predictions: ", '\033[0m')
    print("Here is some percentages and information derived from the predictions of the algorithm")
    print()
    print("M0:\t1: " + str(format((m0_predict.count(1) / len(m0_predict) * 100), '.2f')) + "%\t2: " + str(
        format((m0_predict.count(2) / len(m0_predict) * 100), '.3f')) + "%\t3: " + str(
        format((m0_predict.count(3) / len(m0_predict) * 100), '.3f')) + "%\t4: " + str(
        format((m0_predict.count(4) / len(m0_predict) * 100), '.3f')) + "%")
    print("M1:\t1: " + str(format((m1_predict.count(1) / len(m1_predict) * 100), '.2f')) + "%\t2: " + str(
        format((m1_predict.count(2) / len(m1_predict) * 100), '.3f')) + "%\t3: " + str(
        format((m1_predict.count(3) / len(m1_predict) * 100), '.3f')) + "%\t4: " + str(
        format((m1_predict.count(4) / len(m1_predict) * 100), '.3f')) + "%")
    print("M2:\t1: " + str(format((m2_predict.count(1) / len(m2_predict) * 100), '.2f')) + "%\t2: " + str(
        format((m2_predict.count(2) / len(m2_predict) * 100), '.3f')) + "%\t3: " + str(
        format((m2_predict.count(3) / len(m2_predict) * 100), '.3f')) + "%\t4: " + str(
        format((m2_predict.count(4) / len(m2_predict) * 100), '.3f')) + "%")
    print("Ovr:\t1: " + str(format((myzk_predictions.count(1) / len(myzk_predictions) * 100), '.2f')) + "%\t2: " + str(
        format((myzk_predictions.count(2) / len(myzk_predictions) * 100), '.3f')) + "%\t3: " + str(
        format((myzk_predictions.count(3) / len(myzk_predictions) * 100), '.3f')) + "%\t4: " + str(
        format((myzk_predictions.count(4) / len(myzk_predictions) * 100), '.3f')) + "%")


def displayInaccuracies(Idxs: list[int], cvtLbls: list[float], result: list[int], tag: str) -> list[int]:
    check_array = (cvtLbls == result)
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
            print(cvtLbls[i], end=", ")
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
    for j in total_incorrect:
        ax_scatter = plt.axes()
        x = []
        for k in range(1, 41):
            x.append(k * interval)
        xPoints = np.array(x)
        yPoints = dataSet[j]

        ax_scatter.set_ylabel("3DMSD")
        ax_scatter.set_xlabel("Time Step,s")

        plt.suptitle(fileNames[counter])
        counter += 1

        plt.plot(xPoints, yPoints, color="red", label="AIfSR")
        plt.legend()

        ax_scatter.set_yscale('log')
        ax_scatter.set_xscale('log')

        ax_scatter.set_zorder(2)
        ax_scatter.set_facecolor('none')
        plt.show()


def createAnalysisDocument(algorithm):
    normalizeFeatures = DoNothingNormalization()
    standardizeFeatures = Extract40ValsRegularInterval()
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

    cvtTrnLbls = convert2dLabelsTo1d(trnLbls)
    cvtTestLbls = convert2dLabelsTo1d(testLbls)
    cvtValLbls = convert2dLabelsTo1d(valLbls)

    algorithm.train(trnData, trnLbls)

    test_result = algorithm.predict(testData)
    train_result = algorithm.predict(trnData)
    valid_result = algorithm.predict(valData)

    print('\033[1m', "Accuracy Measurements:", '\033[0m')
    print("Here is the accuracy of our algorithm when the training set, test set,"
          " and cross validation set is passed in")
    print()
    print("Training Accuracy:", metrics.accuracy_score(cvtTrnLbls, train_result))
    print("Test Accuracy:", metrics.accuracy_score(cvtTestLbls, test_result))
    print("Validation Accuracy:", metrics.accuracy_score(cvtValLbls, valid_result))
    print()
    print()

    print('\033[1m', "Inaccurate Trajectories", '\033[0m')
    print("Here is some more information on the trajectories it predicted incorrectly."
          " It displays the indexes of the incorrect trajectories, "
          "followed by the actual diffusion type and the incorrect predicted diffusion type.")
    print()
    print("1 = Ballistic Diffusion, 2 = Confined Diffusion, 3 = Random Walk, 4 = Very Confined Diffusion")
    print()

    idxs_trn_incor = displayInaccuracies(trnIdxs, cvtTrnLbls, train_result, "training")
    idxs_test_incor = displayInaccuracies(testIdxs, cvtTestLbls, test_result, "testing")
    idxs_valid_incor = displayInaccuracies(valIdxs, cvtValLbls, valid_result, "validation")

    total_incorrect = idxs_trn_incor + idxs_test_incor + idxs_valid_incor
    createIncorGraphs(total_incorrect, dataSet)

    MyzkPredictions(algorithm)
