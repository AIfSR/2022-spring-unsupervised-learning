from typing import List
from features.FeaturesWithNames import FeaturesWithNames
from tckfilereader.Point import Point
from tckfilereader.Points import Points

class PointsWithNames(Points):
    def __init__(self, title: str, pointsList: List[Point] = None) -> None:
        """A Points class stores all the points generated from a tck file"""
        super().__init__(pointsList)
        self.title = title
        

    def getName(self) -> str:
        """Gets the name of these Points"""
        return self.title

    def getFeaturesToInitialize(self) -> FeaturesWithNames:
        """Gets a features object that should be initialized with feature values 
        that represent these points. This Features object has the same name as 
        this object"""
        return FeaturesWithNames(self.title)





