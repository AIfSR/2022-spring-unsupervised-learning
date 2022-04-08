import unittest
import numpy as np
from diffusion_prediction.features.Features import Features
from diffusion_prediction.features.MSDFeatureCreator import MSDFeatureCreator
from diffusion_prediction.features.XFeatureCreator import XFeatureCreator

from diffusion_prediction.tckfilereader.Point import Point
from diffusion_prediction.tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class RateOfChangeFeatureCreatorTest (FeatureCreatorTestBase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return MSDFeatureCreator(XFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the RateOfChangeFeatureCreator"""
        points = Points([
            Point(0,2,3,0),
            Point(1,2,3,1),
            Point(2,2,3,2),
            Point(0,2,3,3),
        ])
        rateOfChangeFeatureCreator = MSDFeatureCreator(XFeatureCreator())

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(6/3)
        self.assertEquals(rateOfChangeFeatureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = MSDFeatureCreator(XFeatureCreator())
        self.assertEquals(str(featureCreator), "MSD:X")

