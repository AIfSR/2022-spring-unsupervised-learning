from abc import ABC
from abc import abstractmethod

from AIfSR_Trajectory_Analysis.features.Features import Features

class DatasetFeaturesBase (ABC):
    """This is the base class for getting features from a dataset. This class 
    provides access to data that has been already converted to features, and the
     labels corresponding to that data"""
    
    @abstractmethod
    def getDatasetOfFeatures(self) -> list[Features]:
        """Gets the dataset when all of the data has been converted to features"""
        pass
    
    @abstractmethod
    def getLabels(self) -> list[list[float]]:
        """Gets the labels for each example in the dataset"""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass
