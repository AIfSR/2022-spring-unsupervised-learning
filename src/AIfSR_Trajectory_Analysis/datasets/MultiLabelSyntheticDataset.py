from typing import List, Tuple
from AIfSR_Trajectory_Analysis.datasets.DatasetBase import DatasetBase
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames

import AIfSR_Trajectory_Analysis.datasets.SyntheticFilePaths as FP
from AIfSR_Trajectory_Analysis.tckfilereader.TCKFileReader import TCKFileReader
from AIfSR_Trajectory_Analysis.datasets.LabeledCategory import LabeledCategory

class MultiLabelSyntheticDataset (DatasetBase):
    def __init__(self) -> None:
        self.tckFileReader = TCKFileReader()
        super().__init__()

    def getCategoriesWithPoints(self) -> List[Tuple[str, List[PointsWithNames]]]:
        """Returns a list of all of the synthetic data split up by the type of
        diffusion occuring in each trajectory"""
        BallisticConfinedPoints = self._getValidPointsFromFilePaths(FP.Limits_0_1au_Speed_0_001Paths) +\
                                     self._getValidPointsFromFilePaths(FP.Limits_0_1au_Speed_001_01Paths) + \
                                     self._getValidPointsFromFilePaths(FP.Limits_0_1au_Speed_0001_001Paths)
        BallisticSimplePoints = self._getValidPointsFromFilePaths(FP.Fast_ballisticFilePaths) + \
                            self._getValidPointsFromFilePaths(FP.Random_ballisticFilePaths) + \
                            self._getValidPointsFromFilePaths(FP.Slow_ballisticFilePaths)
        ConfinementEscapePoints = self._getValidPointsFromFilePaths(FP.Confinement_escapeFilePaths)

        # Specifies the three different categories of trajectories that are to be
        # compared and the points list of points associated with each of these treajectory categories
        MultilabeledCasesCategories = [
            LabeledCategory("BALCD", [1.0, 1.0, 0.0], BallisticConfinedPoints),
            LabeledCategory("BALSD", [1.0, 0.0, 1.0], BallisticSimplePoints),
            LabeledCategory("CE", [0.0, 1.0, 1.0], ConfinementEscapePoints),
        ]
        return MultilabeledCasesCategories

    def _getValidPointsFromFilePaths(self, filePaths:List[str]) -> List[PointsWithNames]:
        """Gets trajectories that have at least 50 points in them because some
        trajectories were mistakes and had very few points."""
        pointsList = []
        for file in filePaths:
            points = self.tckFileReader.get_points_with_name(file)
            if len(points) > 49:
                pointsList.append(points)
        return pointsList

