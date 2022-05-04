
from AIfSR_Trajectory_Analysis.normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from AIfSR_Trajectory_Analysis.features.Features import Features

class ScaleZeroToOne (NormalizeFeaturesBase):
    """Normalizes the dataset by dividing by the maximum magnitude value in the 
    dataset"""
    
    def normalizeToSetOfFeatures(self, setOfFeatures:list[Features]) -> list[Features]:
        """Normalizes the set of features by dividing each value by the largest 
        magnitude value found within all of the features."""
        for singleFeature in setOfFeatures:
            featuresMax = max(singleFeature)
            featuresMin = min(singleFeature)
            featuresRange = featuresMax - featuresMin

            for i in range(len(singleFeature)):
                if featuresRange == 0:
                    singleFeature[i] = 1.0
                else:
                    singleFeature[i] = (singleFeature[i] - featuresMin) / featuresRange
        return setOfFeatures
