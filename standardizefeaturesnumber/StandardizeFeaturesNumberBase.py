from abc import ABC, abstractmethod
from features.Features import Features

class StandardizeFeaturesNumberBase (ABC):
    
    def standardizeSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        standardizedSetOfFeatures = []
        for feature in setOfFeatures:
            standardizedSetOfFeatures.append(self.standardizedSetOfFeatures(feature))
        return standardizedSetOfFeatures

    @abstractmethod
    def standardizeFeature(self, feature:Features) -> Features:
        return self.normalizeToAllFeatures([feature])[0]


