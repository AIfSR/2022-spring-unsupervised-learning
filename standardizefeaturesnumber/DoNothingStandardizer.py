

from features.Features import Features
from standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase


class DoNothingStandardizer (StandardizeFeaturesNumberBase):
    """This Standardizer does nothing to standardize the features. It assumes 
    that the length of each of the features is correct for whatever ML algorithm 
    is going to take the features in"""

    def standardizeFeature(self, feature:Features) -> Features:
        return feature