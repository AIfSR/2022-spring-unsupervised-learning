
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class EWAFeatureCreator (FeatureCreatorBase):

    def __init__(self, featureCreator:FeatureCreatorBase, beta:float=0.9, skipValues:int=5) -> None:
        """Creates an Exponentially weighted average feature creator with the 
        beta passed in. It will skip the first 5 values and replace them all 
        with the sixth value unless a different skipValues parameter is pased 
        in."""
        super().__init__()
        self._featureCreator = featureCreator
        self._beta = beta
        self._skipValues = skipValues

    def get_features(self, points:Points) -> Features:
        """Gets the exponentially weighted average of all of the features 
        generated by the feature creator passed in."""
        origFeatures = self._featureCreator.get_features(points)
        features = points.getFeaturesToInitialize()
        prevVal = 0
        count = 1
        for featureVal in origFeatures:
            val = (self._beta * prevVal + (1 - self._beta) * featureVal) / (1 - self._beta**count)
            if count <= self._skipValues:
                pass
            elif count == self._skipValues + 1:
                for i in range(self._skipValues):
                    features.add_feature_val(val)
                features.add_feature_val(val)
            else:
                features.add_feature_val(val)
            count += 1
            prevVal = val

        return features

    def __str__(self) -> str:
        """String representation of the EWAFeatureCreator class"""
        return "EWA:" + str(self._featureCreator)
