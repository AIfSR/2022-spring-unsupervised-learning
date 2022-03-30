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
from datasets.SyntheticDatasetSubset import SyntheticDatasetSubset
import Utilities

plotFeatures = [
        GraphParameters(
            xFeatureCreator=MSDFeatureCreator(XFeatureCreator),
            xLabel = "MSD: X Speed"),
]
realDataset = MacrophageStageDataset()
syntheticDataset = SyntheticDatasetSubset()

FeaturesOverIndices = FeaturesOverIndices()

def getPicturePathway(diffusionType:str, pointsWithNames:PointsWithNames):
    imagePath = Utilities.getMainDirectory() + "/data/02_01_Simulated_trajectories/Simple_cases/"
    fullFileName = pointsWithNames.title
    fileName = fullFileName.split("/")[-1]
    underscores = 0
    for i in range(len(fileName)-1):
        if fileName[i] == "_":
            underscores += 1
            if underscores == 2:
                fileName = fileName[:i] + fileName[i+1:]

    if diffusionType == "Bal":
        imagePath += "Ballistic_movement/Figures/MSDs " + fileName + " .svg"
    elif diffusionType == "CD":
        imagePath += "Confined_diffusion/Figures/MSDs " + fileName + " .svg"
    elif diffusionType == "RW":
        imagePath += "Random_walk/Figures/MSDs " + fileName + " .svg"
    else:
        imagePath += "Very_confined_diffusion/Figures/MSDs " + fileName + " .svg"
    return imagePath

def createGraphsOfSampleOfSyntheticDataset():
    def plotTrajectory(categoryNumber:int, trajectoryNumber:int):
        FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                        syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][trajectoryNumber],
                                        title=syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][trajectoryNumber].title)
    
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
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              syntheticDataset.getCategoriesWithPoints()[i][1][k],
                                              title=syntheticDataset.getCategoriesWithPoints()[i][1][k].title)

def createGraphsOfRealDataset():
    i = 0;
    j = 0;
    k = 0;
    for i in range(len(realDataset.getCategoriesWithPoints())):
        for k in range(len(realDataset.getCategoriesWithPoints()[i][1])):
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              realDataset.getCategoriesWithPoints()[i][1][k],
                                              title=realDataset.getCategoriesWithPoints()[i][1][k].title)

def createGraphsOfSampleOfRealDataset():
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                      realDataset.getCategoriesWithPoints()[0][1][1],
                                      title=realDataset.getCategoriesWithPoints()[0][1][1].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                      realDataset.getCategoriesWithPoints()[0][1][6],
                                      title=realDataset.getCategoriesWithPoints()[0][1][6].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[0][1][13],
                                          title=realDataset.getCategoriesWithPoints()[0][1][13].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][4],
                                          title=realDataset.getCategoriesWithPoints()[1][1][4].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][8],
                                          title=realDataset.getCategoriesWithPoints()[1][1][8].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][11],
                                          title=realDataset.getCategoriesWithPoints()[1][1][11].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][16],
                                          title=realDataset.getCategoriesWithPoints()[1][1][16].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][2],
                                          title=realDataset.getCategoriesWithPoints()[2][1][2].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][10],
                                          title=realDataset.getCategoriesWithPoints()[2][1][10].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][14],
                                          title=realDataset.getCategoriesWithPoints()[2][1][14].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][18],
                                          title=realDataset.getCategoriesWithPoints()[2][1][18].title)



