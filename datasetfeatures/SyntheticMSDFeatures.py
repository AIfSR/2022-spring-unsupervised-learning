from DatasetFeaturesBase import DatasetFeaturesBase
from features.Features import Features
from datasets.SyntheticDataset import SyntheticDataset
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
import os
import pickle

class SyntheticMSDFeatures (DatasetFeaturesBase):
    """This class provides easy access for all of the MSD values from the 
    Synthetic dataset"""

    def __init__(self):
        dataset = SyntheticDataset()
        categories = dataset.getCategoriesWithPoints()
        featureCreator = ThreeDMSDFeatureCreator()

    def getDatasetOfFeatures(self) -> list[Features]:
        """Gets the Synthetic dataset after all of the trajectories have been 
        converted to MSD values."""
        if os.exists("data.pkl"):
            dataFile = open("data.pkl", "rb")
            loaded_dataSet = pickle.load(dataFile)
            dataFile.close()
            return loaded_dataSet
        
        # GENERATE MSD VALUES HERE, WRITE RESULTS TO data.pkl
        self.generateDatafiles("data.pkl", "label.pkl")

        dataFile = open("data.pkl", "rb")
        loaded_dataSet = pickle.load(dataFile)
        dataFile.close()
        return loaded_dataSet

    def getLabels(self) -> list[list[float]]:
        """Gets all of the labels of the synthetic dataset."""
        
        if os.exists("label.pkl"):
            labelFile = open("label.pkl", "rb")
            loadedLabels = pickle.load(labelFile)
            labelFile.close()
            return loadedLabels
        
        # GENERATE LABELS HERE, WRITE RESULTS TO data.pkl
        self.generateDatafiles("data.pkl", "label.pkl")
        labelFile = open("label.pkl", "rb")
        loadedLabels = pickle.load(labelFile)
        labelFile.close()
        return loadedLabels

    def generateDatafiles(self, dataFileName:str, labelFileName:str) -> None:
        label_file = open(labelFileName, 'wb')
        data_file = open(dataFileName, 'wb')
        dataSet = []
        labels = []
        numOfLabels = len(self.categories)
        count = 0

        for i in range(numOfLabels):
            for example in self.categories[i][1]:
                dataSet.append(self.featureCreator.get_features(example))
                label = [0] * numOfLabels
                label[i] = 1
                labels.append(label)
                print(count)
                count += 1

        pickle.dump(labels, label_file)
        labelFileName.close()
        pickle.dump(dataSet, data_file)
        dataFileName.close()
