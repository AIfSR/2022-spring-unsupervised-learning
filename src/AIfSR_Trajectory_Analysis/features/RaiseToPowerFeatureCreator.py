from AIfSR_Trajectory_Analysis.features.FeatureCreatorBase import FeatureCreatorBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points

class RaiseToPowerFeatureCreator (FeatureCreatorBase):
    """Creates a feature that just raises the values of another feature to a 
    specified power"""
    def __init__(self, origFeatureCreator:FeatureCreatorBase, power:float) -> None:
        super().__init__()
        self._origFeatureCreator = origFeatureCreator
        self._power = power

    def get_features(self, points:Points) -> Features:
        """Gets all the features in the original feature creator raised to a 
        power"""
        origFeatures = self._origFeatureCreator.get_features(points)
        features = points.getFeaturesToInitialize()
        for featureVal in origFeatures:
            features.add_feature_val(featureVal**self._power)
        return features

    def __str__(self) -> str:
        """This is a feature for range"""
        return "Power: " + str(self._power) + " of " + str(self._origFeatureCreator)