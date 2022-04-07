from diffusion_prediction.features.FeatureCreatorBase import FeatureCreatorBase
from diffusion_prediction.features.Features import Features
from diffusion_prediction.tckfilereader.Points import Points
import math

class PhiFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is the Phi coordinates of the vectors between points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the Phi values as features"""
        features = points.getFeaturesToInitialize()
        prevPoint = points[0]
        for i in range(1, len(points)):
            point = points[i]
            xDiff = point.get_x() - prevPoint.get_x()
            yDiff = point.get_y() - prevPoint.get_y()
            zDiff = point.get_z() - prevPoint.get_z()
            radius = (xDiff**2 + yDiff**2 + zDiff**2)**0.5
            if radius == 0:
                continue
            phi = math.acos(zDiff / radius)
            features.add_feature_val(phi)
            prevPoint = point

        return features

    def __str__(self) -> str:
        """This is a feature for Phis"""
        return "Phi"