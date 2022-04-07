
from diffusion_prediction.normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from diffusion_prediction.features.Features import Features

class DoNothingNormalization (NormalizeFeaturesBase):
    """Does nothing to the Dataset to normalize it."""

    def normalizeToSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        return setOfFeatures