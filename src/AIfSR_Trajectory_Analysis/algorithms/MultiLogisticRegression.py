from typing import Tuple
from AIfSR_Trajectory_Analysis.algorithms.AlgorithmBase import AlgorithmBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from sklearn.linear_model import LogisticRegression as LR
import pickle
from importlib import resources

from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames
import AIfSR_Trajectory_Analysis.Utilities as Utilities


class MultiLogisticRegression(AlgorithmBase):
    def __init__(self) -> None:
        super().__init__()
        self._model = LR(multi_class='multinomial', solver='lbfgs', max_iter=13000)

    def train(self, trainingData: list[Features], labels: list[list[float]]) -> None:
        y = []
        for i in labels:
            if i == [1.0, 0.0, 0.0]:
                y.append(1)
            elif i == [0.0, 1.0, 0.0]:
                y.append(2)
            elif i == [0.0, 0.0, 1.0]:
                y.append(3)
        self._model.fit(trainingData, y)

    def predict(self, testData: list[FeaturesWithNames]) -> list[Tuple[str, list[float]]]:
        y_pred = self._model.predict(testData)
        y = []
        for i in range(len(y_pred)):
            predictionNum = y_pred[i]
            name = testData[i].getName()
            prediction = [0.0, 0.0, 0.0]
            if predictionNum == 1:
                prediction = [1.0, 0.0, 0.0]
            elif predictionNum == 2:
                prediction = [0.0, 1.0, 0.0]
            elif predictionNum == 3:
                prediction = [0.0, 0.0, 1.0]
            y.append((name, prediction))
        return y

    def predict_prob(self, testData: list[Features]) -> list[Tuple[str,list[float]]]:
        y_pred = self._model.predict_proba(testData)
        y = []
        for i in range(len(y_pred)):
            predictionNum = y_pred[i]
            name = testData[i].getName()
            y.append((name, predictionNum))
        return y

    def save(self, directoryToSaveTo: str, name: str) -> None:
        """Saves the model to the directoryToSaveTo under the name provided"""
        main_dir = Utilities.getMainDirectory()
        location = main_dir + "/" + directoryToSaveTo + "/" + name + ".pkl"
        file = open(location, 'wb')
        pickle.dump(self._model, file)
        file.close()

    def load(self, directory: str, pklFile: str) -> None:
        file = resources.read_binary(directory, pklFile)
        self._model = pickle.loads(file)
