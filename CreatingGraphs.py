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
from tckfilereader.TCKFileReader import TCKFileReader

plotFeatures = [
        GraphParameters(
            xFeatureCreator=MSDFeatureCreator(XFeatureCreator),
            xLabel = "MSD: X Speed"),
]
dataset = MacrophageStageDataset()
dataset1 = SyntheticDataset()

FeaturesOverIndices = FeaturesOverIndices()

def run():
    i = 0;
    j = 0;
    k = 0;
    for i in range(len(dataset1.getCategoriesWithPoints())):
        for k in range(len(dataset1.getCategoriesWithPoints()[i][1])):
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              dataset1.getCategoriesWithPoints()[i][1][k],
                                              dataset1.getCategoriesWithPoints()[i][1][k].title)

def run2():
    i = 0;
    j = 0;
    k = 0;
    for i in range(len(dataset.getCategoriesWithPoints())):
        for k in range(len(dataset.getCategoriesWithPoints()[i][1])):
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              dataset.getCategoriesWithPoints()[i][1][k],
                                              dataset.getCategoriesWithPoints()[i][1][k].title)
