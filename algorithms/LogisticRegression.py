from algorithms.AlgorithmBase import AlgorithmBase
from features.Features import Features
import sklearn

class LogisticRegression(AlgorithmBase):
    def train(trainingData: list[Features], labels: list[list[float]]) -> None:
        pass

    def predict(testData: list[Features]) -> list[list[float]]:
        pass
