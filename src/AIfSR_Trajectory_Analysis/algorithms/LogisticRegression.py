from AIfSR_Trajectory_Analysis.algorithms.AlgorithmBase import AlgorithmBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from sklearn.linear_model import LogisticRegression as LR
import pickle
from importlib import resources

import AIfSR_Trajectory_Analysis.Utilities as Utilities


class LogisticRegression(AlgorithmBase):
    def __init__(self, diffusion_type: str) -> None:
        super().__init__()
        self._model = LR(solver='lbfgs', max_iter=13000)
        self._diffusionType = diffusion_type
        if self._diffusionType == "BAL":
            self._index = 0
        elif self._diffusionType == "CD":
            self._index = 1
        elif self._diffusionType == "RW":
            self._index = 2

    def train(self, trainingData: list[Features], labels: list[list[float]]) -> None:
        y = []
        for i in labels:
            if i[self._index] == 1.0:
                y.append(1)
            else:
                y.append(0)
        self._model.fit(trainingData, y)

    def predict(self, testData: list[Features]) -> list[float]:
        y_pred = self._model.predict(testData)
        return y_pred

    def predict_prob(self, testData:list[Features]) -> list[list[float]]:
        y_pred = self._model.predict_proba(testData)
        y= []
        for feature, prediction in zip(testData, y_pred):
            roundedPrediction = []
            for predictionVal in prediction:
                roundedPrediction.append(round(predictionVal, 3))
            y.append([feature.getName(), roundedPrediction])
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
