from AIfSR_Trajectory_Analysis.features.FeatureCreatorBase import FeatureCreatorBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points


class MultiplyByFactorFeatureCreator (FeatureCreatorBase):
    """Takes a feature and multiplies all of its values by the factor passed in"""

    def __init__(self, featureCreator:FeatureCreatorBase, factor:float) -> None:
        super().__init__()
        self._featureCreator = featureCreator
        self._factor = factor

    def get_features(self, points: Points) -> Features:
        """Gets the features from the original feature creator and multiplies all of the features values
        by the factor passed into the consctructor"""
        features = points.getFeaturesToInitialize()
        originalFeatures = self._featureCreator.get_features(points)

        for featureVal in originalFeatures:
            features.add_feature_val(self._factor * featureVal)

        return features

    def __str__(self) -> str:
        """This is a feature for multiplying by a factor"""
        return str(self._factor) + "*" + str(self._featureCreator)
        