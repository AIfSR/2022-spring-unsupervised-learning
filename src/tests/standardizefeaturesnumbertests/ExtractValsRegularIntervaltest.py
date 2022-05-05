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
        
        extractValsRegularInterval = ExtractValsRegularInterval(80)
        features = extractValsRegularInterval.standardizeFeatures(features)
        self.assertEquals(solution, features)

        features = Features()
        for i in range(801):
            features.add_feature_val(i)
        solution = Features()
        for i in range(80):
            solution.add_feature_val(i*10)
        
        extractValsRegularInterval = ExtractValsRegularInterval(80)
        features = extractValsRegularInterval.standardizeFeatures(features)
        self.assertEquals(solution, features)

        features = Features()
        for i in range(839):
            features.add_feature_val(i)
        solution = Features()
        for i in range(80):
            solution.add_feature_val(i*10)
        
        extractValsRegularInterval = ExtractValsRegularInterval(80)
        features = extractValsRegularInterval.standardizeFeatures(features)
        self.assertEquals(solution, features)

    def test_exception(self):
        features = Features()
        extractValsRegularInterval = ExtractValsRegularInterval(20)
        with self.assertRaises(FeatureStandardizationError):
            extractValsRegularInterval.standardizeFeatures(features)
        for i in range(39):
            features.add_feature_val(i)
        extractValsRegularInterval = ExtractValsRegularInterval(43)
        with self.assertRaises(FeatureStandardizationError):
            extractValsRegularInterval.standardizeFeatures(features)
        features.add_feature_val(5)
        extractValsRegularInterval = ExtractValsRegularInterval(40)
        extractValsRegularInterval.standardizeFeatures(features)

    def test_0Features(self):
        features = Features()
        features.add_feature_val(1)
        features.add_feature_val(2)
        features.add_feature_val(3)
        extractValsRegularInterval = ExtractValsRegularInterval(0)
        features = extractValsRegularInterval.standardizeFeatures(features)
        solution = Features()
        self.assertEquals(solution, features)

