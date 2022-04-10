

from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase


class DoNothingStandardizer (StandardizeFeaturesNumberBase):
    """This Standardizer does nothing to standardize the features. It assumes 
    that the length of each of the features is correct for whatever ML algorithm 
    is going to take the features in"""

    def standardizeFeatures(self, feature:Features) -> Features:
        return feature