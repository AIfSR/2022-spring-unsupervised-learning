from abc import ABC, abstractmethod
from typing import Tuple

from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames

class AlgorithmBase (ABC):
    
    @abstractmethod
    def train(self,trainingData:list[Features], labels:list[list[float]]) -> None:
        pass

    @abstractmethod
    def predict(self,testData:list[FeaturesWithNames]) -> list[Tuple[str,list[float]]]:
        pass

    @abstractmethod
    def save(self, directoryToSaveTo:str, name:str) -> None:
        pass

    @abstractmethod
    def load(self, pathToPklFile:str) -> None:
        pass