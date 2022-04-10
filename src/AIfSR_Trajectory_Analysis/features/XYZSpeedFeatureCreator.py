from AIfSR_Trajectory_Analysis.features.FeatureCreatorBase import FeatureCreatorBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.ABSFeatureCreator import ABSFeatureCreator
from AIfSR_Trajectory_Analysis.features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from AIfSR_Trajectory_Analysis.features.XFeatureCreator import XFeatureCreator
from AIfSR_Trajectory_Analysis.features.YFeatureCreator import YFeatureCreator
from AIfSR_Trajectory_Analysis.features.ZFeatureCreator import ZFeatureCreator
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points

class XYZSpeedFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is the speed of X, Y and Z of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the XYZ speed of all of the points"""
        xSpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())).get_features(points)
        ySpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())).get_features(points)
        zSpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(ZFeatureCreator())).get_features(points)
        features = points.getFeaturesToInitialize()
        for xSpeed, ySpeed, zSpeed in zip(xSpeedFeatures, ySpeedFeatures, zSpeedFeatures):
            totalSpeed = (xSpeed**2 + ySpeed**2 + zSpeed**2)**0.5
            features.add_feature_val(totalSpeed)

        return features

    def __str__(self) -> str:
        """This is a feature for XYZ Speed"""
        return "XYZSpeed"