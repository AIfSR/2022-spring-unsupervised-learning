from abc import ABC, abstractmethod

from features.Features import Features

class AlgorithmBase (ABC):
    
    @abstractmethod
    def train(trainingData:list[Features], labels:list[list[float]]) -> None:
        pass

    @abstractmethod
    def save(fileLocation:str) -> None:
        pass

    @abstractmethod
    def load(fileLocation:str) -> None:
        pass

    @abstractmethod
    def predict(testData:list[Features]) -> list[list[float]]:
        pass