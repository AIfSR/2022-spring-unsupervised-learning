from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.ExtractValsRegularInterval import ExtractValsRegularInterval

class Extract40ValsRegularInterval (StandardizeFeaturesNumberBase):

    def standardizeFeatures(self, features:Features) -> Features:
        """Takes a feature and takes 40 values from that feature at a regular 
        interval"""
        return ExtractValsRegularInterval().standardizeFeatures(features, 40)
        