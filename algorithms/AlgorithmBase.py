from abc import ABC, abstractmethod

from features.Features import Features

class AlgorithmBase (ABC):
    
    @abstractmethod
    def train(self,trainingData:list[Features], labels:list[list[float]]) -> None:
        pass

    @abstractmethod
    def predict(self,testData:list[Features]) -> list[list[float]]:
        pass

    @abstractmethod
    def save(self, directoryToSaveTo:str, name:str) -> None:
        pass

    @abstractmethod
    def load(self, pathToPklFile:str) -> None:
        pass