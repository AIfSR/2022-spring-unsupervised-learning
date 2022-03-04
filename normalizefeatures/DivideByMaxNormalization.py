
from normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from features.Features import Features

class DivideByMaxNormalization (NormalizeFeaturesBase):
    """Normalizes the dataset by dividing by the maximum magnitude value in the 
    dataset"""
    
    def normalizeToSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        """Normalizes the set of features by dividing each value by the largest 
        magnitude value found within all of the features."""
        maxMagnitude = 0
        for singleFeature in setOfFeatures:
            featuresMax = max(singleFeature)
            featuresMin = min(singleFeature)
            if featuresMax > abs(featuresMin):
                maxFeatureMagnitude = featuresMax
            else:
                maxFeatureMagnitude = abs(featuresMin)
            if maxMagnitude < maxFeatureMagnitude:
                maxMagnitude = maxFeatureMagnitude
        
        scaledSet = []
        for features in setOfFeatures:
            scaledFeatures = Features()
            for featureVal in features:
                scaledFeatures.add_feature_val(featureVal / maxMagnitude)
            scaledSet.append(scaledFeatures)
        
        return scaledSet