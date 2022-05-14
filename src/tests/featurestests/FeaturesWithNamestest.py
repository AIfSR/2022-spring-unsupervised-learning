import unittest
from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames

class FeaturesWithNamesTest (unittest.TestCase):

    def test_getName(self):
        featuresWithNames = FeaturesWithNames("name")
        self.assertEquals(featuresWithNames.getName(), "name")

    def test_add(self):
        featuresWithNames = FeaturesWithNames("name")
        featuresWithNames.add_feature_val(1)
        featuresWithNames2 = FeaturesWithNames("name")
        featuresWithNames2.add_feature_val(2)

        solution = FeaturesWithNames("name")
        solution.add_feature_val(1)
        solution.add_feature_val(2)
        featuresWithNames += featuresWithNames2
        self.assertEquals(featuresWithNames, solution)

        featuresWithNames3 = FeaturesWithNames("name2")
        with self.assertRaises(ValueError):
            featuresWithNames+=featuresWithNames3
