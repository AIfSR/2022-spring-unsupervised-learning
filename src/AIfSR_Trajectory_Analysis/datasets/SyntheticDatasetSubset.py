from typing import List, Tuple
from AIfSR_Trajectory_Analysis.datasets.DatasetBase import DatasetBase
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames

import AIfSR_Trajectory_Analysis.datasets.SmallerSetSyntheticFilePaths as FPSubset
from AIfSR_Trajectory_Analysis.tckfilereader.TCKFileReader import TCKFileReader
from AIfSR_Trajectory_Analysis.datasets.LabeledCategory import LabeledCategory

class SyntheticDatasetSubset (DatasetBase):
    def __init__(self) -> None:
        self.tckFileReader = TCKFileReader()
        super().__init__()

    def getCategoriesWithPoints(self) -> List[Tuple[str, List[PointsWithNames]]]:
        """Returns a list of some of the synthetic data split up by the type of 
        diffusion occuring in each trajectory"""
        Ballistic_movementPoints = self._getValidPointsFromFilePaths(FPSubset.Ballistic_movementFilePaths)
        Confined_diffusionPoints = self._getValidPointsFromFilePaths(FPSubset.Confined_diffusionFilePaths)
        Random_walkPoints = self._getValidPointsFromFilePaths(FPSubset.Random_walkFilePaths)
        Very_confined_diffusionPoints = self._getValidPointsFromFilePaths(FPSubset.Very_confined_diffusionFilePaths)

        # Specifies the three different categories of trajectories that are to be
        # compared and the points list of points associated with each of these treajectory categories
        SimpleCasesCategories = [
            LabeledCategory("Bal", [1.0, 0.0, 0.0], Ballistic_movementPoints),
            LabeledCategory("CD", [0.0, 1.0, 0.0], Confined_diffusionPoints),
            LabeledCategory("RW", [0.0, 0.0, 1.0], Random_walkPoints),
            LabeledCategory("VCD", [0.0, 1.0, 0.0], Very_confined_diffusionPoints)
        ]
        return SimpleCasesCategories

    def _getValidPointsFromFilePaths(self, filePaths:List[str]) -> List[PointsWithNames]:
        """Gets trajectories that have at least 50 points in them because some
        trajectories were mistakes and had very few points."""
        pointsList = []
        for file in filePaths:
            points = self.tckFileReader.get_points_with_name(file)
            if len(points) > 49:
                pointsList.append(points)
        return pointsList
