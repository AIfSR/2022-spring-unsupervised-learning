from diffusion_prediction.features.Features import Features
from diffusion_prediction.normalizefeatures.DivideByMaxNormalization import DivideByMaxNormalization
import unittest

class DivideByMaxNormalizationTest (unittest.TestCase):
    """Test class for the DivideByMaxNormalization class"""
    
    def test_normalizeToSetOfFeatures(self) -> None:
        """Tests that a set of features are all scaled by the largest value in 
        the set"""
        feature1 = Features()
        feature1.add_feature_val(1)
        feature1.add_feature_val(2)
        feature1.add_feature_val(3)
        feature2 = Features()
        feature2.add_feature_val(4)
        feature2.add_feature_val(5)
        inputList = [feature1, feature2]
        solutionFeature1 = Features()
        solutionFeature1.add_feature_val(1 / 5)
        solutionFeature1.add_feature_val(2 / 5)
        solutionFeature1.add_feature_val(3 / 5)
        solutionFeature2 = Features()
        solutionFeature2.add_feature_val(4 / 5)
        solutionFeature2.add_feature_val(5 / 5)
        solutionList = [solutionFeature1, solutionFeature2]

        divideByMaxNormalization = DivideByMaxNormalization()
        inputList = divideByMaxNormalization.normalizeToSetOfFeatures(inputList)
        assert solutionList == inputList
    
    def test_normalizeFeature(self) -> None:
        """Tests that a feature is normalized by its largest value"""
        feature = Features()
        feature.add_feature_val(1)
        feature.add_feature_val(2)
        feature.add_feature_val(3)
        solution = Features()
        solution.add_feature_val(1 / 3)
        solution.add_feature_val(2 / 3)
        solution.add_feature_val(3 / 3)

        divideByMaxNormalization = DivideByMaxNormalization()
        feature = divideByMaxNormalization.normalizeFeature(feature)
        assert solution == feature