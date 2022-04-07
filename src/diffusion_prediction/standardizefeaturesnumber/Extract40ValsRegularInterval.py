from diffusion_prediction.features.Features import Features
from diffusion_prediction.standardizefeaturesnumber.FeatureStandardizationError import FeatureStandardizationError
from diffusion_prediction.standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase

class Extract40ValsRegularInterval (StandardizeFeaturesNumberBase):

    def standardizeFeatures(self, features:Features) -> Features:
        """Takes a feature and takes 40 values from that feature at a regular 
        interval"""
        if len(features) < 40:
            raise FeatureStandardizationError()
        featureWith40Vals = Features()
        featureLength = len(features)
        interval = featureLength // 40
        for i in range(40):
            featureWith40Vals.add_feature_val(features[i*interval])
        features.clear()
        for featureVal in featureWith40Vals:
            features.add_feature_val(featureVal)
        return features