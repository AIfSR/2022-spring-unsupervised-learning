import os

NAME_TO_SEARCH_FOR = "src"
path = os.path.dirname(os.path.abspath(__file__))
_mainDirectory = path.split("/")
print("_mainDirectory: ", _mainDirectory)
print("path: " , path)
indexOfDir = _mainDirectory.index(NAME_TO_SEARCH_FOR)
_mainDirectory = _mainDirectory[0:indexOfDir+1]
_mainDirectory = "/".join(_mainDirectory)
_mainDirectory += "/diffusion_prediction"

def getMainDirectory():
    return _mainDirectory

