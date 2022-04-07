from algorithms.AlgorithmBase import AlgorithmBase
from algorithms.LogisticRegression import LogisticRegression
from features.FeatureCreatorBase import FeatureCreatorBase
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from ml_pipelines.MLPipelineBase import MLPipelineBase
from normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from normalizefeatures.ScaletoMillion import ScaletoMillion
from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval
from standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase

class LRPipelineFactory (MLPipelineBase):
    def __init__(self) -> None:
        self._featureCreator = ThreeDMSDFeatureCreator()
        self._featureNormalizer = ScaletoMillion()
        self._featureStandardizer = Extract40ValsRegularInterval()
        self._algorithm = LogisticRegression()
        self._algorithm.load("algorithms/LR_V1.0.pkl")
        super().__init__()
    
    def getFeatureCreator(self) -> FeatureCreatorBase:
        """Gets the 3D MSD Feature creator to extract MSD Values"""
        return self._featureCreator

    def getFeatureNormalizer(self) -> NormalizeFeaturesBase:
        """Gets the ScaleToMillion feature normalizer because this scaling 
        allows the LR algorithm to differentiate between diffusion types the 
        best"""
        return self._featureNormalizer

    def getFeatureStandardizer(self) -> StandardizeFeaturesNumberBase:
        """Gets the Extract 40 vals Regular Interval standardizer, because the 
        logistic regression algorithm does not need more than 40 MSD values"""
        return self._featureStandardizer

    def getAlgorithm(self) -> AlgorithmBase:
        """Gets the logistic regression algorithm"""
        return self._algorithm