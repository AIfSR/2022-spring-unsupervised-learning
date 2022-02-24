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
import matplotlib.pyplot as plt

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
    imagePath = "data/Simple_cases/"
    fullFileName = pointsWithNames.title
    fileName = fullFileName.split("/")[-1]
    if diffusionType == "Bal":
        imagePath += "Ballistic_movement/Figures/MSDs " + fileName + " .svg"
    elif diffusionType == "CD":
        imagePath += "Confined_diffusion/Figures/MSDs " + fileName + " .svg"
    elif diffusionType == "RW":
        imagePath += "Random_walk/Figures/MSDs " + fileName + " .svg"
    else:
        imagePath += "Very_confined_diffusion/Figures/MSDs " + fileName + " .svg"
    return imagePath

def run0():
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

def run():
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

def run2():
    i = 0;
    j = 0;
    k = 0;
    for i in range(len(realDataset.getCategoriesWithPoints())):
        for k in range(len(realDataset.getCategoriesWithPoints()[i][1])):
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              realDataset.getCategoriesWithPoints()[i][1][k],
                                              realDataset.getCategoriesWithPoints()[i][1][k].title)

def run3():
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
