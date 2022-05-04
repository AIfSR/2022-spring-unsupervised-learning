from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.FeatureStandardizationError import FeatureStandardizationError
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase

class ExtractValsRegularInterval (StandardizeFeaturesNumberBase):

    def standardizeFeatures(self, features:Features, numberOfVals:int) -> Features:
        """Takes a feature and takes 40 values from that feature at a regular 
        interval"""
        if(numberOfVals <= 0):
            features.clear()
            return features
        if len(features) < numberOfVals:
            raise FeatureStandardizationError()
        featureWithLessVals = Features()
        featureLength = len(features)
        interval = featureLength // numberOfVals
        for i in range(numberOfVals):
            featureWithLessVals.add_feature_val(features[i*interval])
        features.clear()
        for featureVal in featureWithLessVals:
            features.add_feature_val(featureVal)
        return features