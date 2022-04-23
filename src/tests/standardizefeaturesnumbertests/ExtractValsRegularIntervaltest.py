from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.ExtractValsRegularInterval import ExtractValsRegularInterval
import unittest

from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.FeatureStandardizationError import FeatureStandardizationError

class extractValsRegularIntervalTest (unittest.TestCase):
    """Test class for the extractValsRegularInterval Standardizer"""

    def test_standardizeFeatures(self) -> None:
        """Tests the standardizeFeatures Method"""

        features = Features()
        for i in range(800):
            features.add_feature_val(i)
        solution = Features()
        for i in range(80):
            solution.add_feature_val(i*10)
        
        extractValsRegularInterval = ExtractValsRegularInterval()
        features = extractValsRegularInterval.standardizeFeatures(features, 80)
        self.assertEquals(solution, features)

        features = Features()
        for i in range(801):
            features.add_feature_val(i)
        solution = Features()
        for i in range(80):
            solution.add_feature_val(i*10)
        
        extractValsRegularInterval = ExtractValsRegularInterval()
        features = extractValsRegularInterval.standardizeFeatures(features, 80)
        self.assertEquals(solution, features)

        features = Features()
        for i in range(839):
            features.add_feature_val(i)
        solution = Features()
        for i in range(80):
            solution.add_feature_val(i*10)
        
        extractValsRegularInterval = ExtractValsRegularInterval()
        features = extractValsRegularInterval.standardizeFeatures(features,80)
        self.assertEquals(solution, features)

    def test_exception(self):
        features = Features()
        extractValsRegularInterval = ExtractValsRegularInterval()
        with self.assertRaises(FeatureStandardizationError):
            extractValsRegularInterval.standardizeFeatures(features, 20)
        for i in range(39):
            features.add_feature_val(i)
        with self.assertRaises(FeatureStandardizationError):
            extractValsRegularInterval.standardizeFeatures(features, 43)
        features.add_feature_val(5)
        extractValsRegularInterval.standardizeFeatures(features, 40)

    def test_0Features(self):
        features = Features()
        features.add_feature_val(1)
        features.add_feature_val(2)
        features.add_feature_val(3)
        extractValsRegularInterval = ExtractValsRegularInterval()
        features = extractValsRegularInterval.standardizeFeatures(features, 0)
        solution = Features()
        self.assertEquals(solution, features)

