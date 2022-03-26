from DatasetFeaturesBase import DatasetFeaturesBase
from features.Features import Features
import os
import pickle

class SyntheticMSDFeatures (DatasetFeaturesBase):
    """This class provides easy access for all of the MSD values from the 
    Synthetic dataset"""

    def getDatasetOfFeatures() -> list[Features]:
        """Gets the Synthetic dataset after all of the trajectories have been 
        converted to MSD values."""
        if(os.exists("data.pkl")):
            dataFile = open("data.pkl", "rb")
            loaded_dataSet = pickle.load(dataFile)
            dataFile.close()
            return loaded_dataSet
        
        # GENERATE MSD VALUES HERE, WRITE RESULTS TO data.pkl

    def getLabels() -> list[list[float]]:
        """Gets all of the labels of the synthetic dataset."""
        
        if(os.exists("label.pkl")):
            labelFile = open("label.pkl", "rb")
            loadedLabels = pickle.load(labelFile)
            labelFile.close()
            return loadedLabels
        
        # GENERATE LABELS HERE, WRITE RESULTS TO data.pkl