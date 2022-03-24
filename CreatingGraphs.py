from typing import List
from datasets.MacrophageStageDataset import MacrophageStageDataset
from datasets.SyntheticDataset import SyntheticDataset
from features.MSDFeatureCreator import MSDFeatureCreator
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from features.MarkWhenFeatureValuesChange import MarkWhenFeatureValuesChange
from features.OutlierFeatureCreator import OutlierFeatureCreator
from features.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator
from features.ABSFeatureCreator import ABSFeatureCreator
from features.EWAFeatureCreator import EWAFeatureCreator
from features.EliminatePointsOutsideRangeFeatureCreator import EliminatePointsOutsideRangeFeatureCreator
from features.FeatureCreatorBase import FeatureCreatorBase
from features.PhiFeatureCreator import PhiFeatureCreator
from features.PointsAngleFeatureCreator import PointsAngleFeatureCreator
from features.RaiseToPowerFeatureCreator import RaiseToPowerFeatureCreator
from features.SignChangeFeatureCreator import SignChangeFeatureCreator
from features.SpreadFeatureCreator import SpreadFeatureCreator
from features.ThetaFeatureCreator import ThetaFeatureCreator
from features.XYSpeedFeatureCreator import XYSpeedFeatureCreator
from features.XYZSpeedFeatureCreator import XYZSpeedFeatureCreator
from featuretosingleval.AverageOfFeature import AverageOfFeature
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from featuretosingleval.MedianOfFeature import MedianOfFeature
from plotting.GraphParameters import GraphParameters
from plotting.singlepointcomparetrajectories.SinglePoint2DCompareTrajectories import SinglePoint2DCompareTrajectories
from plotting.singlepointcomparetrajectories.SinglePointCompareTrajectoriesFactory import SinglePointCompareTrajectoriesFactory
from plotting.FeaturesOverIndices import FeaturesOverIndices
import numpy
import numpy as np
import pickle
import matplotlib.pyplot as plt
from normalizefeatures.DoNothingNormalization import DoNothingNormalization
import sklearn.linear_model
from algorithms.LogisticRegression import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval

from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator
from features.TFeatureCreator import TFeatureCreator
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator
from features.PointsDisplacementFeatureCreator import PointsDisplacementFeatureCreator
from tckfilereader.Points import Points
from tckfilereader.PointsWithNames import PointsWithNames
from tckfilereader.TCKFileReader import TCKFileReader

plotFeatures = [
        GraphParameters(
            xFeatureCreator=MSDFeatureCreator(XFeatureCreator),
            xLabel = "MSD: X Speed"),
]
realDataset = MacrophageStageDataset()
syntheticDataset = SyntheticDataset()

FeaturesOverIndices = FeaturesOverIndices()

def getPicturePathway(diffusionType:str, pointsWithNames:PointsWithNames):
    imagePath = "data/02_01_Simulated_trajectories/Simple_cases/"
    fullFileName = pointsWithNames.title
    fileName = fullFileName.split("/")[-1]
    underscores = 0
    for i in range(len(fileName)-1):
        if fileName[i] == "_":
            underscores += 1
            if underscores == 2:
                fileName = fileName[:i] + fileName[i+1:]

    if diffusionType == "Bal":
        imagePath += "Ballistic_movement/Figures/MSDs " + fileName + ".svg"
    elif diffusionType == "CD":
        imagePath += "Confined_diffusion/Figures/MSDs " + fileName + ".svg"
    elif diffusionType == "RW":
        imagePath += "Random_walk/Figures/MSDs " + fileName + ".svg"
    else:
        imagePath += "Very_confined_diffusion/Figures/MSDs " + fileName + ".svg"
    return imagePath

def createGraphsOfSampleOfSyntheticDataset():
    def plotTrajectory(categoryNumber:int, trajectoryNumber:int):
        imagePath = getPicturePathway(syntheticDataset.getCategoriesWithPoints()[categoryNumber][0], syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][trajectoryNumber])
        FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                        syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][trajectoryNumber],
                                        imagePath,
                                        syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][trajectoryNumber].title)
    
    plotTrajectory(0, 0)
    plotTrajectory(1, 44)
    plotTrajectory(2, 39)
    plotTrajectory(3, 43)

def createGraphsOfSyntheticDataset():
    i = 0;
    j = 0;
    k = 0;

    for i in range(len(syntheticDataset.getCategoriesWithPoints())):
        for k in range(len(syntheticDataset.getCategoriesWithPoints()[i][1])):
            imagePath = getPicturePathway(syntheticDataset.getCategoriesWithPoints()[i][0], syntheticDataset.getCategoriesWithPoints()[i][1][k])
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              syntheticDataset.getCategoriesWithPoints()[i][1][k],
                                              imagePath,
                                              syntheticDataset.getCategoriesWithPoints()[i][1][k].title)

def createGraphsOfRealDataset():
    i = 0;
    j = 0;
    k = 0;
    for i in range(len(realDataset.getCategoriesWithPoints())):
        for k in range(len(realDataset.getCategoriesWithPoints()[i][1])):
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              realDataset.getCategoriesWithPoints()[i][1][k],
                                              realDataset.getCategoriesWithPoints()[i][1][k].title)

def createGraphsOfSampleOfRealDataset():
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                      realDataset.getCategoriesWithPoints()[0][1][1],
                                      realDataset.getCategoriesWithPoints()[0][1][1].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                      realDataset.getCategoriesWithPoints()[0][1][6],
                                      realDataset.getCategoriesWithPoints()[0][1][6].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[0][1][13],
                                          realDataset.getCategoriesWithPoints()[0][1][13].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][4],
                                          realDataset.getCategoriesWithPoints()[1][1][4].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][8],
                                          realDataset.getCategoriesWithPoints()[1][1][8].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][11],
                                          realDataset.getCategoriesWithPoints()[1][1][11].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][16],
                                          realDataset.getCategoriesWithPoints()[1][1][16].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][2],
                                          realDataset.getCategoriesWithPoints()[2][1][2].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][10],
                                          realDataset.getCategoriesWithPoints()[2][1][10].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][14],
                                          realDataset.getCategoriesWithPoints()[2][1][14].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][18],
                                          realDataset.getCategoriesWithPoints()[2][1][18].title)



def LRTests(indices:List[int]):
    def plotTrajectory(categoryNumber: int, trajectoryNumber: int):
        imagePath = getPicturePathway(syntheticDataset.getCategoriesWithPoints()[categoryNumber][0], syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][trajectoryNumber])
        FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][
                                              trajectoryNumber],
                                          imagePath,
                                          syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][
                                              trajectoryNumber].title)
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

def createLRGraphs():
    dataset = SyntheticDataset()
    categories = dataset.getCategoriesWithPoints()
    normalizeFeatures = DoNothingNormalization()
    standardizeFeatures = Extract40ValsRegularInterval()
    featureCreator = ThreeDMSDFeatureCreator()
    algorithm = LogisticRegression()

    labelFile = open("label.pkl", "rb")
    loadedLabels = pickle.load(labelFile)
    labelFile.close()
    dataFile = open("data.pkl", "rb")
    loaded_dataSet = pickle.load(dataFile)
    dataFile.close()

    dataSet = normalizeFeatures.normalizeToSetOfFeatures(loaded_dataSet)
    dataSet = standardizeFeatures.standardizeSetOfFeatures(loaded_dataSet)

    indices = np.arange(len(dataSet))
    (
        X_train,
        X_rem,
        y_train,
        y_rem,
        indices_train,
        indices_rem,
    ) = train_test_split(dataSet, loadedLabels, indices, train_size=0.6, random_state=1)

    (
        X_test,
        X_valid,
        y_test,
        y_valid,
        indices_test,
        indices_valid,
    ) = train_test_split(X_rem, y_rem, indices_rem, test_size=0.5, random_state=2)

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

    algorithm.train(X_train, y_train)

    test_result = algorithm.predict(X_test)
    train_result = algorithm.predict(X_train)
    valid_result = algorithm.predict(X_valid)

    print('\033[1m',"Accuracy Measurements:",'\033[0m')
    print("Here is the accuracy of our algorithm when the training set, test set, and cross validation set is passed in")
    print()
    print("Training Accuracy:", metrics.accuracy_score(yTrain, train_result))
    print("Test Accuracy:", metrics.accuracy_score(yTest, test_result))
    print("Validation Accuracy:", metrics.accuracy_score(yValid, valid_result))
    print()
    print()
    print('\033[1m',"Inaccurate Trajectories",'\033[0m')
    print("Here is some more information on the trajectories it predicted incorrectly. It displays the indexes of the incorrect trajectories, followed by the actual diffusion type and the incorrect predicted diffusion type.")
    print()
    print("1 = Ballistic Diffusion, 2 = Confined Diffusion, 3 = Random Walk, 4 = Very Confined Diffusion")
    print()
    training_check_array = (yTrain == train_result)
    testing_check_array = (yTest == test_result)
    validation_check_array = (yValid == valid_result)
    training_incorrect = []
    testing_incorrect = []
    validation_incorrect = []
    indices_training_incorrect = []
    indices_testing_incorrect = []
    indices_validation_incorrect = []
    for index, g in enumerate(training_check_array):
        if not g:
            training_incorrect.append(index)
    for index, g in enumerate(testing_check_array):
        if not g:
            testing_incorrect.append(index)
    for index, g in enumerate(validation_check_array):
        if not g:
            validation_incorrect.append(index)
    for i in training_incorrect:
        indices_training_incorrect.append(indices_train[i])
    for i in testing_incorrect:
        indices_testing_incorrect.append(indices_test[i])
    for i in validation_incorrect:
        indices_validation_incorrect.append(indices_valid[i])
    total_incorrect = indices_training_incorrect + indices_testing_incorrect + indices_validation_incorrect

    # sum = len(training_incorrect) + len(testing_incorrect) + len(validation_incorrect)
    # if sum != 0:
    #     fig, ax = plt.subplots(sum, squeeze=False)
    #     ax = ax.flatten()
    #     i = 0
    #     while i < sum:
    #         for j in indices_training_incorrect:
    #             interval = len(loaded_dataSet[j]) // 40
    #             x = []
    #             for k in range(1, 41):
    #                 x.append(k * interval)
    #             xPoints = np.array(x)
    #             yPoints = dataSet[j]
    #             ax[i].set_yscale('log')
    #             ax[i].set_xscale('log')
    #             ax[i].plot(xPoints, yPoints)
    #             i += 1
    #         for j in indices_testing_incorrect:
    #             interval = len(loaded_dataSet[j]) // 40
    #             x = []
    #             for k in range(1, 41):
    #                 x.append(k * interval)
    #             xPoints = np.array(x)
    #             yPoints = dataSet[j]
    #             ax[i].set_yscale('log')
    #             ax[i].set_xscale('log')
    #             ax[i].plot(xPoints, yPoints)
    #             i += 1
    #         for j in indices_validation_incorrect:
    #             interval = len(loaded_dataSet[j]) // 40
    #             x = []
    #             for k in range(1, 41):
    #                 x.append(k * interval)
    #             xPoints = np.array(x)
    #             yPoints = dataSet[j]
    #             ax[i].set_yscale('log')
    #             ax[i].set_xscale('log')
    #             ax[i].plot(xPoints, yPoints)
    #             i += 1
    #     plt.show

    if len(training_incorrect) != 0:
        print("Indexes of incorrect predictions in training: ")
        for i in indices_training_incorrect:
            print(i,end=", ")
        print()
        print("Actual Diffusion Types: ")
        for i in training_incorrect:
            print(yTrain[i], end=", ")
        print()
        print("Incorrect predictions: ")
        for i in training_incorrect:
            print(train_result[i], end=", ")
        print()
        print()

    if len(testing_incorrect) != 0:
        print("Indexes of incorrect predictions in testing: ")
        for i in indices_testing_incorrect:
            print(i,end=", ")
        print()
        print("Actual Diffusion Types: ")
        for i in testing_incorrect:
            print(yTest[i], end=", ")
        print()
        print("Incorrect predictions: ")
        for i in testing_incorrect:
            print(test_result[i], end=", ")
        print()
        print()

    if len(validation_incorrect) != 0:
        print("Indexes of incorrect predictions in validation: ")
        for i in indices_validation_incorrect:
            print(i, end=", ")
        print()
        print("Actual Diffusion Types: ")
        for i in validation_incorrect:
            print(yValid[i], end=", ")
        print()
        print("Incorrect predictions: ")
        for i in validation_incorrect:
            print(valid_result[i], end=", ")
        print()
        print()

    fileNames = LRTests(total_incorrect)
    interval = 1198 // 40
    counter = 0
    print('\033[1m', "Graphs of Incorrect Trajectories:", '\033[0m')
    print("Here is the graphs of the trajectories that were predicted incorrectly")

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
    myzkdataFile = open("Mzykdata.pkl", "rb")
    loaded_mzyk_dataSet = pickle.load(myzkdataFile)
    myzkdataFile.close()
    mzykdataSet = normalizeFeatures.normalizeToSetOfFeatures(loaded_mzyk_dataSet)
    myzkdataSet = standardizeFeatures.standardizeSetOfFeatures(loaded_mzyk_dataSet)
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
