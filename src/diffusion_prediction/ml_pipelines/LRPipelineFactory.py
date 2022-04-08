from diffusion_prediction.algorithms.AlgorithmBase import AlgorithmBase
from diffusion_prediction.algorithms.LogisticRegression import LogisticRegression
from diffusion_prediction.features.FeatureCreatorBase import FeatureCreatorBase
from diffusion_prediction.features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from diffusion_prediction.ml_pipelines.MLPipelineBase import MLPipelineBase
from diffusion_prediction.normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from diffusion_prediction.normalizefeatures.ScaletoMillion import ScaletoMillion
from diffusion_prediction.standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval
from diffusion_prediction.standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase
import diffusion_prediction.Utilities as Utilities
from importlib import resources

class LRPipelineFactory (MLPipelineBase):
    def __init__(self) -> None:
        self._featureCreator = ThreeDMSDFeatureCreator()
        self._featureNormalizer = ScaletoMillion()
        self._featureStandardizer = Extract40ValsRegularInterval()
        self._algorithm = LogisticRegression()
        self._algorithm.load("diffusion_prediction", "LR_V1.0.pkl")
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