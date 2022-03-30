from DatasetFeaturesBase import DatasetFeaturesBase
from features.Features import Features
from datasets.MacrophageStageDataset import MacrophageStageDataset
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
import os
import pickle


class MzykMSDFeatures(DatasetFeaturesBase):
    """This class provides easy access for all of the MSD values from the
    Synthetic dataset"""

    def __init__(self):
        dataset = MacrophageStageDataset()
        categories = dataset.getCategoriesWithPoints()
        featureCreator = ThreeDMSDFeatureCreator()

    def getDatasetOfFeatures(self) -> list[Features]:
        """Gets the Synthetic dataset after all of the trajectories have been
        converted to MSD values."""
        if os.exists("Mzykdata.pkl"):
            dataFile = open("Myzkdata.pkl", "rb")
            loaded_dataSet = pickle.load(dataFile)
            dataFile.close()
            return loaded_dataSet

        # GENERATE MSD VALUES HERE, WRITE RESULTS TO data.pkl
        self.generateDatafiles("Myzkdata.pkl")

        dataFile = open("Myzkdata.pkl", "rb")
        loaded_dataSet = pickle.load(dataFile)
        dataFile.close()
        return loaded_dataSet

    def generateDatafiles(self, dataFileName:str) -> None:
        data_file = open(dataFileName, 'wb')
        dataSet = []
        count = 0
        for i in range(len(self.categories)):
            for example in self.categories[i][1]:
                dataSet.append(self.featureCreator.get_features(example))
                print(count)
                count += 1
        pickle.dump(dataSet, data_file)
        data_file.close()

