
from normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from features.Features import Features

class DoNothingNormalization (NormalizeFeaturesBase):
    """Does nothing to the Dataset to normalize it."""

    def normalizeToSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        return setOfFeatures