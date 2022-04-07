from diffusion_prediction.features.FeatureCreatorBase import FeatureCreatorBase
from diffusion_prediction.features.Features import Features
from diffusion_prediction.features.ABSFeatureCreator import ABSFeatureCreator
from diffusion_prediction.features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from diffusion_prediction.features.XFeatureCreator import XFeatureCreator
from diffusion_prediction.features.YFeatureCreator import YFeatureCreator
from diffusion_prediction.tckfilereader.Points import Points

class XYSpeedFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is the speed of X and Y of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the XY speed of all of the points"""
        xSpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())).get_features(points)
        ySpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())).get_features(points)
        features = points.getFeaturesToInitialize()
        for xSpeed, ySpeed in zip(xSpeedFeatures, ySpeedFeatures):
            totalSpeed = (xSpeed**2 + ySpeed**2)**0.5
            features.add_feature_val(totalSpeed)

        return features

    def __str__(self) -> str:
        """This is a feature for XY Speed"""
        return "XYSpeed"