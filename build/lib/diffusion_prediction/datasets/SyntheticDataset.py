from typing import List, Tuple
from diffusion_prediction.datasets.DatasetBase import DatasetBase
from diffusion_prediction.tckfilereader.Points import Points
from diffusion_prediction.tckfilereader.PointsWithNames import PointsWithNames

import diffusion_prediction.datasets.SyntheticFilePaths as FP
from diffusion_prediction.tckfilereader.TCKFileReader import TCKFileReader


class SyntheticDataset (DatasetBase):
    def __init__(self) -> None:
        self.tckFileReader = TCKFileReader()
        super().__init__()

    def getCategoriesWithPoints(self) -> List[Tuple[str, List[PointsWithNames]]]:
        """Returns a list of all of the synthetic data split up by the type of 
        diffusion occuring in each trajectory"""
        Ballistic_movementPoints = self._getValidPointsFromFilePaths(FP.Ballistic_movementFilePaths)
        Confined_diffusionPoints = self._getValidPointsFromFilePaths(FP.Confined_diffusionFilePaths)
        Random_walkPoints = self._getValidPointsFromFilePaths(FP.Random_walkFilePaths)
        Very_confined_diffusionPoints = self._getValidPointsFromFilePaths(FP.Very_confined_diffusionFilePaths)

        # Specifies the three different categories of trajectories that are to be
        # compared and the points list of points associated with each of these treajectory categories
        SimpleCasesCategories = [
            ("Bal", Ballistic_movementPoints),
            ("CD", Confined_diffusionPoints),
            ("RW", Random_walkPoints),
            ("VCD", Very_confined_diffusionPoints),
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
