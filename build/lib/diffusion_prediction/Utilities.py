import os
from DirName import DIR_NAME

_mainDirectory = os.getcwd()
path = os.path.dirname(os.path.abspath(__file__))

_mainDirectory = _mainDirectory.replace('datasets','')
_mainDirectory = _mainDirectory.split("/")
indexOfDir = _mainDirectory.index(DIR_NAME)
_mainDirectory = _mainDirectory[0:indexOfDir+1]
_mainDirectory = "/".join(_mainDirectory)
_mainDirectory += "/src/diffusion_prediction"
def getMainDirectory():
    return _mainDirectory

