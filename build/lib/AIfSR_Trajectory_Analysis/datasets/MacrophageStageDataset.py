from typing import List, Tuple
from AIfSR_Trajectory_Analysis.datasets.DatasetBase import DatasetBase
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames
import AIfSR_Trajectory_Analysis.datasets.RealFilePaths as FP
from AIfSR_Trajectory_Analysis.tckfilereader.TCKFileReader import TCKFileReader


class MacrophageStageDataset (DatasetBase):

    def __init__(self) -> None:
        self.tckFileReader = TCKFileReader()
        super().__init__()

    def getCategoriesWithPoints(self) -> List[Tuple[str, List[PointsWithNames]]]:
        """Returns a list of all of Real's data split up by m0, m1, and m2"""
        m0Points = self._getValidPointsFromFilePaths(FP.m0FilePaths)
        m1Points = self._getValidPointsFromFilePaths(FP.m1FilePaths)
        m2Points = self._getValidPointsFromFilePaths(FP.m2FilePaths)
        
        # Specifies the three different categories of trajectories that are to be 
        # compared and the points list of points associated with each of these treajectory categories
        stageCategories = [
            ("M0", m0Points),
            ("M1", m1Points),
            ("M2", m2Points),
        ]
        return stageCategories
    
    def _getValidPointsFromFilePaths(self, filePaths:List[str]) -> List[PointsWithNames]:
        """Gets trajectories that have at least 50 points in them because some 
        trajectories were mistakes and had very few points."""
        pointsList = []
        for file in filePaths:
            points = self.tckFileReader.get_points_with_name(file)
            if len(points) > 50:
                pointsList.append(points)
        return pointsList
