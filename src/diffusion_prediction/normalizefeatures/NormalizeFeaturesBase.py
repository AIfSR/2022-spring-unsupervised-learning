from abc import ABC, abstractmethod
from features.Features import Features

class NormalizeFeaturesBase (ABC):
    
    @abstractmethod
    def normalizeToSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        """Takes a list of features and normalizes each feature relative to all 
        of the other features in the list"""
        pass

    def normalizeFeature(self, feature:Features) -> Features:
        """Takes a single Features object and normalizes all of the values in 
        that features object, relative to itself"""
        return self.normalizeToSetOfFeatures([feature])[0]