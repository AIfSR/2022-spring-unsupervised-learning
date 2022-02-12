from typing import List
from datasets.MacrophageStageDataset import MacrophageStageDataset
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

if __name__ == "__main__":

    # PlotFeatures stores all of the GraphParameters associated with each desired graph. 
    # In this case there will be 5 graphs, the first one will plot the average X speed 
    # against the average Y speed of the trajectories passed in in a scatterplot, and the next two will 
    # plot similar 2 dimensional graphs but with different features for the X and Y axes.
    # The fourth GraphParameters object only has an xFeatureCreator set which means it will only 
    # plot one dimension in the form of a boxplot. The final GraphParameters object similarly only 
    # plots one dimension in the form of a boxplot but in this case it is taking the median value of 
    # the angle between points as opposed to the average value
    plotFeatures = [
        GraphParameters(
            xFeatureCreator=ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())), 
            yFeatureCreator=ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), 
            yLabel = "Average: Y Speed",
            xLabel = "Average: X Speed"),
        GraphParameters(
            xFeatureCreator=ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())), 
            yFeatureCreator=ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), 
            featuresToSingleVal=MedianOfFeature()),
        GraphParameters(
            xFeatureCreator=PointsAngleFeatureCreator(),
            yFeatureCreator=RateOfChangeFeatureCreator(PointsDistanceFeatureCreator())),    
        GraphParameters(
            xFeatureCreator=PointsAngleFeatureCreator()),
        GraphParameters(
            xFeatureCreator=PointsAngleFeatureCreator(),
            featuresToSingleVal=MedianOfFeature()),
    ]

    # The MacrophageStageDataset is all of the real points split up by macrophage
    # stage: M0, M1, M2
    dataset = MacrophageStageDataset()

    # Takes all of the points and categories specified above in the stageCategories variable, 
    # and all of the different types of graphs specified above in the plotFeatures variable and 
    # creates all of the desired graphs one at a time.
    singlePoint2DCompareTrajectoriesFactory = SinglePointCompareTrajectoriesFactory()
    singlePoint2DCompareTrajectoriesFactory.display_plots(plotFeatures, dataset.getCategoriesWithPoints())


