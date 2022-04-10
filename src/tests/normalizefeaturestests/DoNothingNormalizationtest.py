from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.normalizefeatures.DoNothingNormalization import DoNothingNormalization
import unittest

class DoNothingNormalizationTest (unittest.TestCase):
    """Test class for the DoNothingNormalization class"""
    
    def test_normalizeToSetOfFeatures(self) -> None:
        """Tests that nothing is done to normalize a set of features"""
        feature1 = Features()
        feature1.add_feature_val(1)
        feature1.add_feature_val(2)
        feature1.add_feature_val(3)
        feature2 = Features()
        feature2.add_feature_val(4)
        feature2.add_feature_val(5)
        inputList = [feature1, feature2]
        solutionFeature1 = Features()
        solutionFeature1.add_feature_val(1)
        solutionFeature1.add_feature_val(2)
        solutionFeature1.add_feature_val(3)
        solutionFeature2 = Features()
        solutionFeature2.add_feature_val(4)
        solutionFeature2.add_feature_val(5)
        solutionList = [solutionFeature1, solutionFeature2]

        doNothingNormalization = DoNothingNormalization()
        inputList = doNothingNormalization.normalizeToSetOfFeatures(inputList)
        self.assertEquals(solutionList, inputList)
