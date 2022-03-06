from features.Features import Features
from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval
import unittest

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