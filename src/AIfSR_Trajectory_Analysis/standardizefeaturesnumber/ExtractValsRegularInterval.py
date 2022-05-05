from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.FeatureStandardizationError import FeatureStandardizationError
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase

class ExtractValsRegularInterval (StandardizeFeaturesNumberBase):
    def __init__(self, numberOfVals:int) -> None:
        self.numberOfVals = numberOfVals

    def standardizeFeatures(self, features:Features) -> Features:
        """Takes a feature and takes 40 values from that feature at a regular 
        interval"""
        if(self.numberOfVals <= 0):
            features.clear()
            return features
        if len(features) < self.numberOfVals:
            raise FeatureStandardizationError()
        featureWithLessVals = Features()
        featureLength = len(features)
        interval = featureLength // self.numberOfVals
        for i in range(self.numberOfVals):
            featureWithLessVals.add_feature_val(features[i*interval])
        features.clear()
        for featureVal in featureWithLessVals:
            features.add_feature_val(featureVal)
        return features