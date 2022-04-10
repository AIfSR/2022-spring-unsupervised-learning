
from AIfSR_Trajectory_Analysis.normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from AIfSR_Trajectory_Analysis.features.Features import Features

class DoNothingNormalization (NormalizeFeaturesBase):
    """Does nothing to the Dataset to normalize it."""

    def normalizeToSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        return setOfFeatures