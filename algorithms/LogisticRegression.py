from algorithms.AlgorithmBase import AlgorithmBase
from features.Features import Features
from sklearn.linear_model import LogisticRegression as LR
import numpy as np


class LogisticRegression(AlgorithmBase):
    def __init__(self) -> None:
        super().__init__()
        self._model = LR(multi_class='multinomial', solver='lbfgs', max_iter=13000)

    def train(self, trainingData: list[Features], labels: list[list[float]]) -> None:
        y = []
        for i in labels:
            if i == [1.0, 0.0, 0.0, 0.0]:
                y.append(1)
            elif i == [0.0, 1.0, 0.0, 0.0]:
                y.append(2)
            elif i == [0.0, 0.0, 1.0, 0.0]:
                y.append(3)
            elif i == [0.0, 0.0, 0.0, 1.0]:
                y.append(4)
        labels_arr = np.array(y)
        self._model.fit(trainingData, y)

    def predict(self, testData: list[Features]) -> list[list[float]]:
        y_pred = self._model.predict(testData)
        y = []
        for i in y_pred:
            if i == 1:
                y.append([1.0, 0.0, 0.0, 0.0])
            elif i == 2:
                y.append([0.0, 1.0, 0.0, 0.0])
            elif i == 3:
                y.append([0.0, 0.0, 1.0, 0.0])
            else:
                y.append([0.0, 0.0, 0.0, 1.0])
        return y

    def predict_proba(self, testData: list[Features]) -> list[list[float]]:
        y_pred = self._model.predict_proba(testData)
        return y_pred
