from AIfSR_Trajectory_Analysis.features.FeatureCreatorBase import FeatureCreatorBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points

class YFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the Y coordinates of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the Y values as features"""
        features = points.getFeaturesToInitialize()
        for point in points:
            features.add_feature_val(point.get_y())

        return features

    def __str__(self) -> str:
        """This is a feature for Y coords"""
        return "Y"