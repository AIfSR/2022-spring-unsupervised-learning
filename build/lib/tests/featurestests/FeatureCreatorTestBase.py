import unittest
from abc import ABC, abstractmethod
from diffusion_prediction.features.FeatureCreatorBase import FeatureCreatorBase
from diffusion_prediction.features.FeaturesWithNames import FeaturesWithNames
from diffusion_prediction.tckfilereader.Point import Point
from diffusion_prediction.tckfilereader.PointsWithNames import PointsWithNames
from diffusion_prediction.tckfilereader.Points import Points

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


