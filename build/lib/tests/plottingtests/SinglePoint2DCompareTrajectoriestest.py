import unittest

from diffusion_prediction.features.Features import Features
from diffusion_prediction.plotting.singlepointcomparetrajectories.SinglePoint2DCompareTrajectories import SinglePoint2DCompareTrajectories
from diffusion_prediction.plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator
from diffusion_prediction.featuretosingleval.AverageOfFeature import AverageOfFeature
from diffusion_prediction.tckfilereader.Point import Point
from diffusion_prediction.tckfilereader.Points import Points

class SinglePoint2DCompareTrajectoriesTest (unittest.TestCase):

    def test_calculate_hist_height(self) -> None:
        """Tests calculating the height for each histogram"""

        solution = (1.0 - (SinglePoint2DCompareTrajectories.BOTTOM * 2 + SinglePoint2DCompareTrajectories.HEIGHT + 2 * SinglePoint2DCompareTrajectories.SPACING)) / 2
        singlePointCompareTrajectories = SinglePoint2DCompareTrajectories()
        self.assertAlmostEquals(solution, singlePointCompareTrajectories._calculate_hist_height(2))


