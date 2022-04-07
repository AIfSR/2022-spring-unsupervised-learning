from abc import ABC, abstractmethod
from typing import Tuple

from features.Features import Features
from features.FeaturesWithNames import FeaturesWithNames

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