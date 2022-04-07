from datasetfeatures.DatasetFeaturesBase import DatasetFeaturesBase
from features.Features import Features
from datasets.SyntheticDataset import SyntheticDataset
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
import os
import pickle
import Utilities


class SyntheticMSDFeatures(DatasetFeaturesBase):
    """This class provides easy access for all of the MSD values from the 
    Synthetic dataset"""

    def __init__(self):
        dataset = SyntheticDataset()
        self.categories = dataset.getCategoriesWithPoints()
        self.featureCreator = ThreeDMSDFeatureCreator()
        mainDir = Utilities.getMainDirectory()
        self._dataFilePath = mainDir + "/data/data.pkl"
        self._labelFilePath = mainDir + "/data/label.pkl"

    def _bothFilesExist(self) -> bool:
        return os.path.exists(self._dataFilePath) and os.path.exists(self._labelFilePath)

    def getDatasetOfFeatures(self) -> list[Features]:
        """Gets the Synthetic dataset after all of the trajectories have been
        converted to MSD values."""
   
        if not self._bothFilesExist():
            self.generateDatafiles()

        dataFile = open(self._dataFilePath, "rb")
        loaded_dataSet = pickle.load(dataFile)
        dataFile.close()
        return loaded_dataSet

    def getLabels(self) -> list[list[float]]:
        """Gets all of the labels of the synthetic dataset."""
        if not self._bothFilesExist():
            self.generateDatafiles()

        labelFile = open(self._labelFilePath, "rb")
        loadedLabels = pickle.load(labelFile)
        labelFile.close()
        return loadedLabels

    def generateDatafiles(self) -> None:
        label_file = open(self._labelFilePath, 'wb')
        data_file = open(self._dataFilePath, 'wb')
        dataSet = []
        labels = []
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
                label = [0] * numOfLabels
                label[i] = 1
                labels.append(label)
                if (count / (totalTrajectories // 10)) % 1 == 0:
                    print(str(count) + "/" + str(totalTrajectories) + " MSD vals calculated")
                count += 1

        pickle.dump(labels, label_file)
        label_file.close()
        pickle.dump(dataSet, data_file)
        data_file.close()