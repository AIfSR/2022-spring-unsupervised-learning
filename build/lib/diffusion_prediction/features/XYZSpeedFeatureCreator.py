from diffusion_prediction.features.FeatureCreatorBase import FeatureCreatorBase
from diffusion_prediction.features.Features import Features
from diffusion_prediction.features.ABSFeatureCreator import ABSFeatureCreator
from diffusion_prediction.features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from diffusion_prediction.features.XFeatureCreator import XFeatureCreator
from diffusion_prediction.features.YFeatureCreator import YFeatureCreator
from diffusion_prediction.features.ZFeatureCreator import ZFeatureCreator
from diffusion_prediction.tckfilereader.Points import Points

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