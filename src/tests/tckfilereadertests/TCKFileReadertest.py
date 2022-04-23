import unittest
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames
from AIfSR_Trajectory_Analysis.tckfilereader.TCKFileReader import TCKFileReader
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from AIfSR_Trajectory_Analysis.tckfilereader.Point import Point

class TCKFileReaderTest (unittest.TestCase):

    def test_get_points(self):
        """Tests getting points from a tck file"""
        path = "src/tests/tckfilereadertests/testfile2.txt"
        tckFileReader = TCKFileReader()
        solutionPoints = PointsWithNames(path)
        solutionPoints.addPoint(Point(1,6,11,16))
        solutionPoints.addPoint(Point(2,7,12,17))
        solutionPoints.addPoint(Point(3,8,13,18))
        solutionPoints.addPoint(Point(4,9,14,19))
        solutionPoints.addPoint(Point(5,10,15,20))
        testPoints = tckFileReader.get_points_with_name(path, tckFileInDirectory=False)
        self.assertEquals(testPoints, solutionPoints)

