import unittest
import numpy as np
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.MSDFeatureCreator import MSDFeatureCreator
from AIfSR_Trajectory_Analysis.features.XFeatureCreator import XFeatureCreator

from AIfSR_Trajectory_Analysis.tckfilereader.Point import Point
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
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


