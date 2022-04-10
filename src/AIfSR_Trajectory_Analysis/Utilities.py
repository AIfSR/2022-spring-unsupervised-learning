import os

NAME_TO_SEARCH_FOR = "src"
path = os.path.dirname(os.path.abspath(__file__))
_mainDirectory = path.split("/")
try:
    indexOfDir = _mainDirectory.index(NAME_TO_SEARCH_FOR)
    _mainDirectory = _mainDirectory[0:indexOfDir+1]
    _mainDirectory = "/".join(_mainDirectory)
    _mainDirectory += "/AIfSR_Trajectory_Analysis"
except:
    _mainDirectory = "/".join(_mainDirectory)

def getMainDirectory():
    return _mainDirectory

