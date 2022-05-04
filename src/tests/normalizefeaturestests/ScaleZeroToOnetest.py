from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.normalizefeatures.ScaleZeroToOne import ScaleZeroToOne
import unittest

class ScaleZeroToOneTest (unittest.TestCase):
    """Test class for the scaleZeroToOne class"""
    
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
        solutionFeature1.add_feature_val(0)
        solutionFeature1.add_feature_val(1/2)
        solutionFeature1.add_feature_val(1)
        solutionFeature2 = Features()
        solutionFeature2.add_feature_val(0)
        solutionFeature2.add_feature_val(1)
        solutionList = [solutionFeature1, solutionFeature2]

        scaleZeroToOne = ScaleZeroToOne()
        inputList = scaleZeroToOne.normalizeToSetOfFeatures(inputList)
        assert solutionList == inputList
    
    def test_normalizeFeature(self) -> None:
        """Tests that a feature is normalized by its largest value"""
        feature = Features()
        feature.add_feature_val(1)
        feature.add_feature_val(2)
        feature.add_feature_val(3)
        solution = Features()
        solution.add_feature_val(0)
        solution.add_feature_val(1/2)
        solution.add_feature_val(1)

        scaleZeroToOne = ScaleZeroToOne()
        feature = scaleZeroToOne.normalizeFeature(feature)
        assert solution == feature