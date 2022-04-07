from diffusion_prediction.features.FeatureCreatorBase import FeatureCreatorBase
from diffusion_prediction.features.Features import Features
from diffusion_prediction.features.TFeatureCreator import TFeatureCreator
from diffusion_prediction.features.XFeatureCreator import XFeatureCreator
from diffusion_prediction.features.YFeatureCreator import YFeatureCreator
from diffusion_prediction.features.ZFeatureCreator import ZFeatureCreator
from diffusion_prediction.tckfilereader.Points import Points
import numpy as np


class ThreeDMSDFeatureCreator(FeatureCreatorBase):
    """Gets the MSD trajectories in all three dimensions"""

    def __init__(self) -> None:
        super().__init__()

    def get_features(self, points:Points) -> Features:
        """Gets the MSD in three dimensions of the points"""
        features = points.getFeaturesToInitialize()
        timeFeature = TFeatureCreator().get_features(points)
        xFeature = XFeatureCreator().get_features(points)
        yFeature = YFeatureCreator().get_features(points)
        zFeature = ZFeatureCreator().get_features(points)

        N = len(timeFeature)
        
        MSDinX = np.array(xFeature[0:N])
        x = xFeature._featuresList
        DispX = np.zeros((N, N)).astype('float64')
        for k in range(1,N):
            for i in range(N - k):
                DispX[k, i] = (x[i] - x[i + k]) ** 2

        for j in range(N):
            MSDinX[j] = np.sum(DispX[j, 0:N - j]) / (N - j)

        MSDinY = np.array(yFeature[0:N])
        y = yFeature._featuresList
        DispY = np.zeros((N, N)).astype('float64')
        for k in range(1,N):
            for i in range(N - k):
                DispY[k, i] = (y[i] - y[i + k]) ** 2

        for j in range(N):
            MSDinY[j] = np.sum(DispY[j, 0:N - j]) / (N - j)
        MSDinZ = np.array(zFeature[0:N])

        z = zFeature._featuresList
        DispZ = np.zeros((N, N)).astype('float64')
        for k in range(1,N):
            for i in range(N - k):
                DispZ[k, i] = (z[i] - z[i + k]) ** 2

        for j in range(N):
            MSDinZ[j] = np.sum(DispZ[j, 0:N - j]) / (N - j)

        result = MSDinX + MSDinY + MSDinZ
        for k in result:
            features.add_feature_val(k)

        # This code is here because the first value is always 0 because it is 
        # finding the displacement between every point and itself, and the last 
        # two points are unreliable because the MSD is only averaged over 1 or 2 
        # points within the trajectory
        features._featuresList = features._featuresList[1:-2]
        
        return features


    def __str__(self) -> str:
        """This is a feature for the Mean Squared Displacement"""
        return "3DMSD"


