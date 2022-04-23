import unittest

from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.plotting.singlepointcomparetrajectories.SinglePoint2DCompareTrajectories import SinglePoint2DCompareTrajectories
from AIfSR_Trajectory_Analysis.plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator
from AIfSR_Trajectory_Analysis.featuretosingleval.AverageOfFeature import AverageOfFeature
from AIfSR_Trajectory_Analysis.tckfilereader.Point import Point
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points

class SinglePoint2DCompareTrajectoriesTest (unittest.TestCase):

    def test_calculate_hist_height(self) -> None:
        """Tests calculating the height for each histogram"""

        solution = (1.0 - (SinglePoint2DCompareTrajectories.BOTTOM * 2 + SinglePoint2DCompareTrajectories.HEIGHT + 2 * SinglePoint2DCompareTrajectories.SPACING)) / 2
        singlePointCompareTrajectories = SinglePoint2DCompareTrajectories()
        self.assertAlmostEquals(solution, singlePointCompareTrajectories._calculate_hist_height(2))


