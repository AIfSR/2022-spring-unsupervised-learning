from datasetfeatures.DatasetFeaturesBase import DatasetFeaturesBase
from features.Features import Features
from datasets.MacrophageStageDataset import MacrophageStageDataset
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
import os
import pickle
import Utilities


class MzykMSDFeatures(DatasetFeaturesBase):
    """This class provides easy access for all of the MSD values from the
    real dataset"""

    def __init__(self):
        dataset = MacrophageStageDataset()
        self.categories = dataset.getCategoriesWithPoints()
        self.featureCreator = ThreeDMSDFeatureCreator()
        mainDir = Utilities.getMainDirectory()
        self._dataFilePath = mainDir + "/data/Mzykdata.pkl"

    def getDatasetOfFeatures(self) -> list[Features]:
        """Gets the Synthetic dataset after all of the trajectories have been
        converted to MSD values."""
        if not os.path.exists(self._dataFilePath):
            self.generateDatafiles()
        
        dataFile = open(self._dataFilePath, "rb")
        loaded_dataSet = pickle.load(dataFile)
        dataFile.close()
        return loaded_dataSet

    def getLabels(self) -> list[list[float]]:
        """Gets the labels for each example in the dataset"""
        pass

    def generateDatafiles(self) -> None:
        data_file = open(self._dataFilePath, 'wb')
        dataSet = []
        numOfLabels = len(self.categories)
        count = 0

        totalTrajectories = 0
        for i in range(numOfLabels):
            for example in self.categories[i][1]:
                totalTrajectories += 1

        print("Generating MSD Files")

        for i in range(numOfLabels):
            for example in self.categories[i][1]:
                dataSet.append(self.featureCreator.get_features(example))
                if (count / (totalTrajectories // 10)) % 1 == 0:
                    print(str(count) + "/" + str(totalTrajectories) + " MSD vals calculated")
                count += 1

        pickle.dump(dataSet, data_file)
        data_file.close()
