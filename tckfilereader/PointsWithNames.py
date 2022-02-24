from typing import List
from tckfilereader.Point import Point
from tckfilereader.Points import Points

class PointsWithNames(Points):
    def __init__(self, title: str, pointsList: List[Point] = None) -> None:
        """A Points class stores all the points generated from a tck file"""
        super().__init__(pointsList)
        self.title = title
        pass






