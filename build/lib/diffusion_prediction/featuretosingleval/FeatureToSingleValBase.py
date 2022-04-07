from abc import ABC, abstractmethod
from diffusion_prediction.features.Features import Features

class FeatureToSingleValBase(ABC):

    @abstractmethod
    def get_val(self, features:Features) -> float:
        """Reduces features representing all of the points in a trajectory down to a single value"""
        pass