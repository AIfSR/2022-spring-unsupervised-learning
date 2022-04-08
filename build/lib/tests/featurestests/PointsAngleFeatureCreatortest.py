import unittest
from diffusion_prediction.features.Features import Features
from diffusion_prediction.features.OutlierFeatureCreator import OutlierFeatureCreator
from diffusion_prediction.features.PointsAngleFeatureCreator import PointsAngleFeatureCreator
from diffusion_prediction.features.XFeatureCreator import XFeatureCreator

from diffusion_prediction.tckfilereader.Point import Point
from diffusion_prediction.tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase
import unittest

class OutlierFeatureCreatorTest (FeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the PointsAngleFeatureCreator to test"""
        return PointsAngleFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the PointsAngle Feature Creator"""
        points = Points([
            Point(0,0,0,1),
            Point(1,0,0,2),
            Point(1,1,0,2),
            Point(1,2,0,2),
            Point(1,-2,0,2),
           
        ])
        featureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(-1)
        
        
        self.assertEquals(featureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "PointsAngle")