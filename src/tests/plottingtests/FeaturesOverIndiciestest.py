import unittest
from AIfSR_Trajectory_Analysis.features.Features import Features

from AIfSR_Trajectory_Analysis.plotting.FeaturesOverIndices import IndiciesFeatureCreator
from AIfSR_Trajectory_Analysis.tckfilereader.Point import Point
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points

class FeaturesOverIndiciesTest (unittest.TestCase):
    def test_get_features(self):
        features = Features()
        for i in range(10):
            features.add_feature_val(i + 10)
        indiciesFeatureCreator = IndiciesFeatureCreator(features)
        answer = indiciesFeatureCreator.get_features(None)
        self.assertEquals(len(answer), 10)
        for solutionVal, answerVal in zip(range(10), answer):
            self.assertEquals(solutionVal, answerVal)
