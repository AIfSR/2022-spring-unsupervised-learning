import unittest
from abc import ABC, abstractmethod
from features.FeatureCreatorBase import FeatureCreatorBase
from features.FeaturesWithNames import FeaturesWithNames
from tckfilereader.Point import Point
from tckfilereader.PointsWithNames import PointsWithNames
from tckfilereader.Points import Points

class FeatureCreatorTestBase (unittest.TestCase):

    @abstractmethod
    def get_feature_creator(self) -> FeatureCreatorBase:
        """Gets the feature creator being tested"""
        pass

    def test_namesArePreserved(self):
        """Tests that when a feature creator is passed in a Points object with a 
        name, it creates a features object with a name"""
        featureCreator = self.get_feature_creator()
        pointsWithNames = PointsWithNames("name")
        pointsWithNames.addPoint(Point(1,2,3,0))
        pointsWithNames.addPoint(Point(1,2,3,1))
        pointsWithNames.addPoint(Point(1,2,3,2))
        features = featureCreator.get_features(pointsWithNames)
        self.assertEquals(type(features), FeaturesWithNames)
        self.assertEquals(features.getName(), "name")


