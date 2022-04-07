from abc import ABC, abstractmethod
from algorithms.AlgorithmBase import AlgorithmBase
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase

class MLPipelineBase (ABC):
    """This is a base class for all factories providing a machine learning 
    pipeline. This class provides access to the feature creator to convert 
    points to features, a normalizer to ensure that the features passed into the
    algorithm are scaled properly, a standardizer to ensure that a standardized
    number of features per occurance are passed into an algorithm, and an 
    algorithm to train or predict with."""

    @abstractmethod
    def getFeatureCreator(self) -> FeatureCreatorBase:
        """Gets the feature creator to convert points in a trajectory to 
        features"""
        pass

    @abstractmethod
    def getFeatureNormalizer(self) -> NormalizeFeaturesBase:
        """Gets the feature normalizer to ensure that all features are in an 
        acceptable range"""
        pass

    @abstractmethod
    def getFeatureStandardizer(self) -> StandardizeFeaturesNumberBase:
        """Gets the feature standardizer to ensure that each occurence has the 
        same number of features"""
        pass

    @abstractmethod
    def getAlgorithm(self) -> AlgorithmBase:
        """Gets the algorithm to process the data"""
        pass