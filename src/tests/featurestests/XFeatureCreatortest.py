
import unittest
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.XFeatureCreator import XFeatureCreator

from AIfSR_Trajectory_Analysis.tckfilereader.Point import Point
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase


class XFeatureCreatorTest (FeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return XFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the X Feature Creator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        xFeatureCreator = XFeatureCreator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(1.0)
        solutionFeatures.add_feature_val(5.0)
        solutionFeatures.add_feature_val(9.0)
        
        answerFeatures = xFeatureCreator.get_features(points)
        a = type(answerFeatures)
        b = type(solutionFeatures)
        
        self.assertEquals(answerFeatures, solutionFeatures)
    
    def test_string(self):
        featureCreator = XFeatureCreator()
        self.assertEquals(str(featureCreator), "X")