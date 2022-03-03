from abc import ABC, abstractmethod
from features.Features import Features

class NormalizeFeaturesBase (ABC):
    
    @abstractmethod
    def normalizeToSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        pass

    def normalizeFeature(self, feature:Features) -> Features:
        return self.normalizeToSetOfFeatures([feature])[0]