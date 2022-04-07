import unittest
from features.Features import Features
from features.MultiplyByFactorFeatureCreator import MultiplyByFactorFeatureCreator
from features.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class RateOfChangeFeatureCreatorTest (FeatureCreatorTestBase):
    def get_feature_creator(self):
        """Gets the MultiplyByFactorFeatureCreator to test"""
        return MultiplyByFactorFeatureCreator(XFeatureCreator(), 2.0)

    def test_get_features(self):
        """Tests getting features from the MultiplyByFactorFeatureCreator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        multiplyByFactorFeatureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(2)
        solutionFeatures.add_feature_val(10)
        solutionFeatures.add_feature_val(18)
        
        self.assertEquals(multiplyByFactorFeatureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "2.0*X")
