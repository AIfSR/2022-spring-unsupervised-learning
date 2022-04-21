from AIfSR_Trajectory_Analysis.datasetfeatures.DatasetFeaturesBase import DatasetFeaturesBase
from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.features.FeaturesWithNames import FeaturesWithNames
from AIfSR_Trajectory_Analysis.datasets.SyntheticDataset import SyntheticDataset
from AIfSR_Trajectory_Analysis.features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
import os
import pickle
import AIfSR_Trajectory_Analysis.Utilities as Utilities
from importlib import resources


class SyntheticMSDFeatures(DatasetFeaturesBase):
    """This class provides easy access for all of the MSD values from the 
    Synthetic dataset"""

    def __init__(self):
        dataset = SyntheticDataset()
        self.categories = dataset.getCategoriesWithPoints()
        self.featureCreator = ThreeDMSDFeatureCreator()
        mainDir = Utilities.getMainDirectory()
        self._directory = mainDir + "/data"
        self._dataFileName = "data.pkl"
        self._labelFileName = "label.pkl"
        self._dataFilePath = self._directory + "/" + self._dataFileName
        self._labelFilePath = self._directory + "/" + self._labelFileName

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
            for example in self.categories[i].trajectories:
                totalTrajectories += 1
        
        print("Generating MSD Files")

        for i in range(numOfLabels):
            for example in self.categories[i].trajectories:
                dataSet.append(self.featureCreator.get_features(example))
                label = self.categories[i].labels
                labels.append(label)
                if (count / (totalTrajectories // 10)) % 1 == 0:
                    print(str(count) + "/" + str(totalTrajectories) + " MSD vals calculated")
                count += 1

        pickle.dump(labels, label_file)
        label_file.close()
        pickle.dump(dataSet, data_file)
        data_file.close()

