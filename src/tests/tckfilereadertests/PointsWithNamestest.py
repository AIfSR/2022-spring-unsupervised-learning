import unittest
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames

class TestPointsWithNames(unittest.TestCase):

    def test_getName(self):
        pointsWithNames = PointsWithNames("name")
        self.assertEquals(pointsWithNames.getName(), "name")

    def test_getFeaturesToInitialize(self):
        pointsWithNames = PointsWithNames("name")
        self.assertEquals(type(pointsWithNames.getFeaturesToInitialize()), FeaturesWithNames)