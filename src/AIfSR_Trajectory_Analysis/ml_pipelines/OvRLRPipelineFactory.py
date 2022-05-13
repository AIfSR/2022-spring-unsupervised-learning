from AIfSR_Trajectory_Analysis.algorithms.AlgorithmBase import AlgorithmBase
from AIfSR_Trajectory_Analysis.algorithms.OvRLogisticRegression import OvRLogisticRegression
from AIfSR_Trajectory_Analysis.features.FeatureCreatorBase import FeatureCreatorBase
from AIfSR_Trajectory_Analysis.features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from AIfSR_Trajectory_Analysis.ml_pipelines.MLPipelineBase import MLPipelineBase
from AIfSR_Trajectory_Analysis.normalizefeatures.DivideByMaxNormalization import DivideByMaxNormalization
from AIfSR_Trajectory_Analysis.normalizefeatures.NormalizeFeaturesBase import NormalizeFeaturesBase
from AIfSR_Trajectory_Analysis.normalizefeatures.ScaletoMillion import ScaletoMillion
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.ExtractValsRegularInterval import ExtractValsRegularInterval
from AIfSR_Trajectory_Analysis.standardizefeaturesnumber.StandardizeFeaturesNumberBase import StandardizeFeaturesNumberBase
import AIfSR_Trajectory_Analysis.Utilities as Utilities
from importlib import resources


class OvRLRPipelineFactory(MLPipelineBase):
    def __init__(self, modelToLoad: str = "OvRLR.pkl") -> None:
        super().__init__(modelToLoad)
        self._featureCreator = ThreeDMSDFeatureCreator()
        self._featureNormalizer = DivideByMaxNormalization()
        self._featureStandardizer = ExtractValsRegularInterval(20)
        self._algorithm = OvRLogisticRegression(0.5)
        self._algorithm.load("AIfSR_Trajectory_Analysis", self._modelToLoad)


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
