import unittest
from features.Features import Features
from features.FeaturesWithNames import FeaturesWithNames
from tckfilereader.PointsWithNames import PointsWithNames

class TestPointsWithNames(unittest.TestCase):

    def test_getName(self):
        pointsWithNames = PointsWithNames("name")
        self.assertEquals(pointsWithNames.getName(), "name")

    def test_getFeaturesToInitialize(self):
        pointsWithNames = PointsWithNames("name")
        self.assertEquals(type(pointsWithNames.getFeaturesToInitialize()), FeaturesWithNames)