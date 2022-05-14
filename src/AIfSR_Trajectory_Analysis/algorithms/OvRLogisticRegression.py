from typing import Tuple
from AIfSR_Trajectory_Analysis.algorithms.AlgorithmBase import AlgorithmBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames
import pickle
from importlib import resources
from AIfSR_Trajectory_Analysis.algorithms.LogisticRegression import LogisticRegression
import AIfSR_Trajectory_Analysis.Utilities as Utilities


class OvRLogisticRegression(AlgorithmBase):
    def __init__(self, threshold: float = 0.5) -> None:
        super().__init__()
        self._BALmodel = LogisticRegression("BAL")
        self._CDmodel = LogisticRegression("CD")
        self._RWmodel = LogisticRegression("RW")
        self._threshold = threshold

    def train(self, trainingData: list[Features], labels: list[list[float]]) -> None:
        BALdata = []
        CDdata = []
        RWdata = []

        for i in labels:
            BALdata.append(int(i[0]))
            CDdata.append(int(i[1]))
            RWdata.append(int(i[2]))

        self._BALmodel.train(trainingData, BALdata)
        self._CDmodel.train(trainingData, CDdata )
        self._RWmodel.train(trainingData, RWdata)

    def getProbabilities(self, testData: list[Features]) -> list[list[float]]:
        result = []
        ba = self._BALmodel.predict_prob(testData)
        cd = self._CDmodel.predict_prob(testData)
        rw = self._RWmodel.predict_prob(testData)
        for i in range(len(ba)):
            result.append([ba[i][1][1], cd[i][1][1], rw[i][1][1]])
        return result

    def predict(self, testData: list[FeaturesWithNames]) -> list[Tuple[str, list[float]]]:
        result = []
        prediction_probabilities = self.getProbabilities(testData)
        for i in range(len(prediction_probabilities)):
            name = testData[i].getName()
            prob_list = []
            for j in prediction_probabilities[i]:
                if j >= self._threshold:
                    prob_list.append(1.0)
                else:
                    prob_list.append(0.0)
            result.append((name, prob_list))
        return result

    def predict_prob(self, testData:list[FeaturesWithNames]) -> list[Tuple[str,list[float]]]:
        result = []
        prediction_probabilities = self.getProbabilities(testData)
        for i in range(len(prediction_probabilities)):
            name = testData[i].getName()
            prob_list = prediction_probabilities[i]
            result.append((name, prob_list))
        return result

    def save(self, directoryToSaveTo: str, name: str) -> None:
        """Saves the model to the directoryToSaveTo under the name provided"""
        main_dir = Utilities.getMainDirectory()
        location = main_dir + "/" + directoryToSaveTo + "/" + name + ".pkl"
        file = open(location, 'wb')
        models = [self._BALmodel, self._CDmodel, self._RWmodel]
        pickle.dump(models, file)
        file.close()

    def load(self, directory: str, pklFile: str) -> None:
        file = resources.read_binary(directory, pklFile)
        models = pickle.loads(file)
        self._BALmodel = models[0]
        self._CDmodel = models[1]
        self._RWmodel = models[2]
