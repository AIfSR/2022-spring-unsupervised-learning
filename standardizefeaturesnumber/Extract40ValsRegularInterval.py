from features.Features import Features
from standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase

class Extract40ValsRegularInterval (StandardizeFeaturesNumberBase):

    def standardizeFeatures(self, features:Features) -> Features:
        """Takes a feature and takes 40 values from that feature at a regular 
        interval"""
        featureWith40Vals = Features()
        featureLength = len(features)
        interval = featureLength // 40
        for i in range(40):
            featureWith40Vals.add_feature_val(features[i*interval])
        return featureWith40Vals