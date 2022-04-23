from typing import List, Tuple
from AIfSR_Trajectory_Analysis.datasets.DatasetBase import DatasetBase
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames

import AIfSR_Trajectory_Analysis.datasets.SyntheticFilePaths as FP
from AIfSR_Trajectory_Analysis.tckfilereader.TCKFileReader import TCKFileReader
from random import sample


class SyntheticDataset (DatasetBase):
    def __init__(self) -> None:
        self.tckFileReader = TCKFileReader()
        super().__init__()

    def getCategoriesWithPoints(self, numberFromEachCategory:int=None) -> List[Tuple[str, List[PointsWithNames]]]:
        """Returns a list of all of the synthetic data split up by the type of 
        diffusion occuring in each trajectory"""
        if(numberFromEachCategory is None):
            Ballistic_movementPoints = self._getValidPointsFromFilePaths(FP.Ballistic_movementFilePaths)
            Confined_diffusionPoints = self._getValidPointsFromFilePaths(FP.Confined_diffusionFilePaths)
            Random_walkPoints = self._getValidPointsFromFilePaths(FP.Random_walkFilePaths)
            Very_confined_diffusionPoints = self._getValidPointsFromFilePaths(FP.Very_confined_diffusionFilePaths)
        else:
            minimumNumberOfTrajecories = min(len(FP.Ballistic_movementFilePaths), 
                len(FP.Confined_diffusionFilePaths), len(FP.Random_walkFilePaths), 
                len(FP.Very_confined_diffusionFilePaths))
            if(numberFromEachCategory > minimumNumberOfTrajecories):
                print("numberFromEachCategory is bigger than the the smallest category of trajectories. Setting it to: ", str(minimumNumberOfTrajecories))
                numberFromEachCategory = minimumNumberOfTrajecories
            Ballistic_movementPoints = self._getValidPointsFromFilePaths(sample(FP.Ballistic_movementFilePaths, numberFromEachCategory))
            Confined_diffusionPoints = self._getValidPointsFromFilePaths(sample(FP.Confined_diffusionFilePaths,numberFromEachCategory))
            Random_walkPoints = self._getValidPointsFromFilePaths(sample(FP.Random_walkFilePaths,numberFromEachCategory))
            Very_confined_diffusionPoints = self._getValidPointsFromFilePaths(sample(FP.Very_confined_diffusionFilePaths,numberFromEachCategory))
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
