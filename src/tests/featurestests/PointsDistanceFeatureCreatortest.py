import unittest
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator
from AIfSR_Trajectory_Analysis.tckfilereader.Point import Point
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class PointsDistanceFeatureCreatorTest (FeatureCreatorTestBase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return PointsDistanceFeatureCreator()

    def test_get_features(self):
        """Tests getting the features from the PointsDistanceFeatureCreator"""
        points = Points([
            Point(0,0,0,1),
            Point(1,0,0,2),
            Point(1,1,0,3),
            Point(0,0,0,4),
            Point(1,1,1,5),
        ])
        pointsDistanceFeatureCreator = PointsDistanceFeatureCreator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(2.0**0.5)
        solutionFeatures.add_feature_val(3.0**0.5)
        # solutionFeatures.add_feature_val(3.0**0.5)
        
        self.assertEquals(pointsDistanceFeatureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = PointsDistanceFeatureCreator()
        self.assertEquals(str(featureCreator), "PointsDistance")


