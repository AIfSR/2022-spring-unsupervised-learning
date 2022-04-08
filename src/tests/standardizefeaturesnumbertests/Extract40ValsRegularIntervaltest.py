from diffusion_prediction.features.Features import Features
from diffusion_prediction.standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval
import unittest

from diffusion_prediction.standardizefeaturesnumber.FeatureStandardizationError import FeatureStandardizationError

class Extract40ValsRegularIntervalTest (unittest.TestCase):
    """Test class for the Extract40ValsRegularInterval Standardizer"""

    def test_standardizeFeatures(self) -> None:
        """Tests the standardizeFeatures Method"""

        features = Features()
        for i in range(400):
            features.add_feature_val(i)
        solution = Features()
        for i in range(40):
            solution.add_feature_val(i*10)
        
        extract40ValsRegularInterval = Extract40ValsRegularInterval()
        features = extract40ValsRegularInterval.standardizeFeatures(features)
        self.assertEquals(solution, features)

        features = Features()
        for i in range(401):
            features.add_feature_val(i)
        solution = Features()
        for i in range(40):
            solution.add_feature_val(i*10)
        
        extract40ValsRegularInterval = Extract40ValsRegularInterval()
        features = extract40ValsRegularInterval.standardizeFeatures(features)
        self.assertEquals(solution, features)

        features = Features()
        for i in range(439):
            features.add_feature_val(i)
        solution = Features()
        for i in range(40):
            solution.add_feature_val(i*10)
        
        extract40ValsRegularInterval = Extract40ValsRegularInterval()
        features = extract40ValsRegularInterval.standardizeFeatures(features)
        self.assertEquals(solution, features)

    def test_exception(self):
        features = Features()
        extract40ValsRegularInterval = Extract40ValsRegularInterval()
        with self.assertRaises(FeatureStandardizationError):
            extract40ValsRegularInterval.standardizeFeatures(features)
        for i in range(39):
            features.add_feature_val(i)
        with self.assertRaises(FeatureStandardizationError):
            extract40ValsRegularInterval.standardizeFeatures(features)
        features.add_feature_val(5)
        extract40ValsRegularInterval.standardizeFeatures(features)