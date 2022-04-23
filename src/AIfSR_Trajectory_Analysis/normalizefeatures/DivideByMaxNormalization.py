
from AIfSR_Trajectory_Analysis.normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from AIfSR_Trajectory_Analysis.features.Features import Features

class DivideByMaxNormalization (NormalizeFeaturesBase):
    """Normalizes the dataset by dividing by the maximum magnitude value in the 
    dataset"""
    
    def normalizeToSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        """Normalizes the set of features by dividing each value by the largest 
        magnitude value found within all of the features."""
        for singleFeature in setOfFeatures:
            featuresMax = max(singleFeature)
            featuresMin = min(singleFeature)
            featuresRange = featuresMax - featuresMin
            if featuresMax > abs(featuresMin):
                maxFeatureMagnitude = featuresMax
            else:
                maxFeatureMagnitude = abs(featuresMin)
            for i in range(len(singleFeature)):
                singleFeature[i] = singleFeature[i] / maxFeatureMagnitude

        return setOfFeatures
