import unittest
from diffusion_prediction.features.Features import Features
from diffusion_prediction.features.YFeatureCreator import YFeatureCreator

from diffusion_prediction.tckfilereader.Point import Point
from diffusion_prediction.tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class YFeatureCreatorTest (FeatureCreatorTestBase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return YFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the Y Feature Creator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        yFeatureCreator = YFeatureCreator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(2)
        solutionFeatures.add_feature_val(6)
        solutionFeatures.add_feature_val(10)
        
        self.assertEquals(yFeatureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = YFeatureCreator()
        self.assertEquals(str(featureCreator), "Y")