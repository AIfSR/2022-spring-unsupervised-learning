

from AIfSR_Trajectory_Analysis.features.FeatureCreatorBase import FeatureCreatorBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points


class PointsDisplacementFeatureCreator (FeatureCreatorBase):

    def get_features(self, points:Points) -> Features:
        """Creates a feature that gets the euclidean distance between every
        point"""
        features = points.getFeaturesToInitialize()
        firstPoint = points[0]
        finalPoint = points[len(points)-1]
        xdifference = finalPoint.get_x() - firstPoint.get_x()
        ydifference = finalPoint.get_y() - firstPoint.get_y()
        zdifference = finalPoint.get_z() - firstPoint.get_z()
        displacement= (xdifference**2 + ydifference**2 + zdifference**2)**0.5
        features.add_feature_val(displacement)
        return features

    def __str__(self) -> str:
        """This is a feature for the distance between points"""
        return "PointsDisplacement"
