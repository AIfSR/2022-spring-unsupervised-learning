import unittest
from abc import ABC, abstractmethod
from AIfSR_Trajectory_Analysis.features.FeatureCreatorBase import FeatureCreatorBase
from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames
from AIfSR_Trajectory_Analysis.tckfilereader.Point import Point
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points

class FeatureCreatorTestBase (unittest.TestCase):

    @abstractmethod
    def get_feature_creator(self) -> FeatureCreatorBase:
        """Gets the feature creator being tested"""
        pass

    def test_namesArePreserved(self):
        """Tests that when a feature creator is passed in a Points object with a 
        name, it creates a features object with a name"""
        
        featureCreator = self.get_feature_creator()
        if not featureCreator == None:
            pointsWithNames = PointsWithNames("name")
            pointsWithNames.addPoint(Point(1,2,3,0))
            pointsWithNames.addPoint(Point(1,2,3,1))
            pointsWithNames.addPoint(Point(1,2,3,2))
            features = featureCreator.get_features(pointsWithNames)
            self.assertEquals(type(features), FeaturesWithNames)
            self.assertEquals(features.getName(), "name")


