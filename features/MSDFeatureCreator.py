from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.TFeatureCreator import TFeatureCreator
from tckfilereader.Points import Points
import numpy as np


class MSDFeatureCreator(FeatureCreatorBase):
    """Takes a feature and finds the MSD of that feature over time"""

    def __init__(self, featureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreator = featureCreator

    def get_features(self, points: Points) -> Features:
        """Gets the MSD of all the values in the feature created"""
        features = Features()
        timeFeature = TFeatureCreator().get_features(points)
        otherFeature = self._featureCreator.get_features(points)

        N = len(timeFeature)
        
        x = otherFeature._featuresList
        DispX = np.zeros((N, N)).astype('float64')
        for k in range(1,N):
            for i in range(N - k):
                DispX[k, i] = (x[i] - x[i + k]) ** 2

        for j in range(N):
            features.add_feature_val(np.sum(DispX[j, 0:N - j]) / (N - j))

        # This code is here because the first value is always 0 because it is 
        # finding the displacement between every point and itself, and the last 
        # two points are unreliable because the MSD is only averaged over 1 or 2 
        # points within the trajectory
        features._featuresList = features._featuresList[1:-2]
        return features


    def __str__(self) -> str:
        """This is a feature for the Mean Squared Displacement of another feature"""
        
        return "MSD:" + str(self._featureCreator)
