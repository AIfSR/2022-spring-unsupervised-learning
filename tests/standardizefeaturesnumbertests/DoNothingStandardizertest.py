from features.Features import Features
from standardizefeaturesnumber.DoNothingStandardizer import DoNothingStandardizer
import unittest

class DoNothingStandardizerTest (unittest.TestCase):
    """Test class for the DoNothingStandardizer"""

    def test_standardizeSetOfFeatures(self) -> None:
        """Tests to make sure that nothing is done to a set of features"""
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

        doNothingStandardizer = DoNothingStandardizer()
        inputList = doNothingStandardizer.standardizeSetOfFeatures(inputList)
        assert solutionList == inputList

    def test_standardizeFeature(self) -> None:
        """Tests to make sure that nothing is done to a singular feature"""
        feature = Features()
        feature.add_feature_val(1)
        feature.add_feature_val(2)
        feature.add_feature_val(3)
        solution = Features()
        solution.add_feature_val(1)
        solution.add_feature_val(2)
        solution.add_feature_val(3)

        doNothingStandardizer = DoNothingStandardizer()
        feature = doNothingStandardizer.standardizeFeatures(feature)
        assert solution == feature

