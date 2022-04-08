import unittest
from diffusion_prediction.features.FeaturesWithNames import FeaturesWithNames

class FeaturesWithNamesTest (unittest.TestCase):

    def test_getName(self):
        featuresWithNames = FeaturesWithNames("name")
        self.assertEquals(featuresWithNames.getName(), "name")