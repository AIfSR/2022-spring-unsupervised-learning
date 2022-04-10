from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points
from abc import ABC, abstractmethod
from AIfSR_Trajectory_Analysis.features.Features import Features

class FeatureCreatorBase (ABC):

    @abstractmethod
    def get_features(self, points:Points) -> Features:
        """Creates and gets the features"""
        pass
    