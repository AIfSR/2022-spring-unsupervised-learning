from diffusion_prediction.normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from diffusion_prediction.features.Features import Features

class ScaletoMillion(NormalizeFeaturesBase):
    """Normalizes the dataset by dividing by the maximum magnitude value in the
    dataset"""

    def normalizeToSetOfFeatures(self, setOfFeatures: list[Features]) -> list[Features]:
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

        for features in setOfFeatures:
            for i in range(len(features)):
                features[i] = (features[i] / maxMagnitude) * (10 ** 8)

        return setOfFeatures
