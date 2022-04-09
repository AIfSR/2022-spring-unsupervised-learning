from typing import Tuple
from diffusion_prediction.algorithms.AlgorithmBase import AlgorithmBase
from diffusion_prediction.features.Features import Features
from sklearn.linear_model import LogisticRegression as LR
import numpy as np
import pickle
from importlib import resources

from diffusion_prediction.features.FeaturesWithNames import FeaturesWithNames
import diffusion_prediction.Utilities as Utilities


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

    def predict(self, testData:list[FeaturesWithNames]) -> list[Tuple[str,list[float]]]:
        y_pred = self._model.predict(testData)
        y = []
        for i in range(len(y_pred)):
            predictionNum = y_pred[i]
            name = testData[i].getName()
            if predictionNum == 1:
                prediction = [1.0, 0.0, 0.0, 0.0]
            elif predictionNum == 2:
                prediction = [0.0, 1.0, 0.0, 0.0]
            elif predictionNum == 3:
                prediction = [0.0, 0.0, 1.0, 0.0]
            else:
                prediction = [0.0, 0.0, 0.0, 1.0]
            y.append((name, prediction))
        return y

    def predict_proba(self, testData: list[Features]) -> list[list[float]]:
        y_pred = self._model.predict_proba(testData)
        return y_pred

    def save(self, directoryToSaveTo:str, name:str) -> None:
        """Saves the model to the directoryToSaveTo under the name provided"""
        main_dir = Utilities.getMainDirectory()
        location = main_dir + "/" + directoryToSaveTo + "/" + name + ".pkl"
        file = open(location, 'wb')
        pickle.dump(self._model, file)
        file.close

    def load(self, directory:str, pklFile:str) -> None:
        file = resources.read_binary(directory, pklFile)
        self._model = pickle.loads(file)