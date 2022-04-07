from diffusion_prediction.tckfilereader.Points import Points
from abc import ABC, abstractmethod
from diffusion_prediction.features.Features import Features

class FeatureCreatorBase (ABC):

    @abstractmethod
    def get_features(self, points:Points) -> Features:
        """Creates and gets the features"""
        pass
    