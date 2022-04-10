import unittest
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.OutlierFeatureCreator import OutlierFeatureCreator
from AIfSR_Trajectory_Analysis.features.PointsAngleFeatureCreator import PointsAngleFeatureCreator
from AIfSR_Trajectory_Analysis.features.XFeatureCreator import XFeatureCreator

from AIfSR_Trajectory_Analysis.tckfilereader.Point import Point
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase
import unittest

class OutlierFeatureCreatorTest (FeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the PointsAngleFeatureCreator to test"""
        return PointsAngleFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the PointsAngle Feature Creator"""
        points = Points([
            Point(0,0,0,1),
            Point(1,0,0,2),
            Point(1,1,0,2),
            Point(1,2,0,2),
            Point(1,-2,0,2),
           
        ])
        featureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(-1)
        
        
        self.assertEquals(featureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "PointsAngle")