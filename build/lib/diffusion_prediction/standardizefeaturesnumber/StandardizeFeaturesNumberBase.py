from abc import ABC, abstractmethod
from diffusion_prediction.features.Features import Features

class StandardizeFeaturesNumberBase (ABC):
    """This is the base class from which standardizers derive from. The length 
    of features needs to be standardized for certain algorithmstests and so the child
    classes of this base class will standardize the features."""

    @abstractmethod
    def standardizeFeatures(self, feature:Features) -> Features:
        """Takes a feature and standardizes the length of that feature to ensure
        that it can be processed by an ML algorithm"""
        pass

    def standardizeSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        """Takes a set of features and standardizes their lengths so that they
        can be processed by an ML algorithm."""
        standardizedSetOfFeatures = []
        for feature in setOfFeatures:
            standardizedSetOfFeatures.append(self.standardizeFeatures(feature))
        return standardizedSetOfFeatures

