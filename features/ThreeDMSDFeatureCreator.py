from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.TFeatureCreator import TFeatureCreator
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator
from tckfilereader.Points import Points
import numpy as np


class ThreeDMSDFeatureCreator(FeatureCreatorBase):
    """Takes a feature and finds the rate of change over all of the values"""

    def __init__(self) -> None:
        super().__init__()

    def get_features(self, points: Points) -> Features:
        features = Features()
        timeFeature = TFeatureCreator().get_features(points)
        xFeature = XFeatureCreator().get_features(points)
        yFeature = YFeatureCreator().get_features(points)
        zFeature = ZFeatureCreator().get_features(points)
        firstVal = True

        N = len(timeFeature)
        """Gets the rate of change of all the values in the feature created"""
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
        # features._featuresList = features._featuresList[:-2]
        # del features._featuresList[0]
        return features

        # for val, time in zip(otherFeature, timeFeature):
        #     if firstVal:
        #         # features.add_feature_val(0.0)
        #         # # this line needs to be here so that there are an equal amount
        #         # # of feature values as points passed in
        #         firstVal = False
        #     else:
        #         valChange = val - prevVal
        #         tChange = time - prevTime
        #         features.add_feature_val((valChange ** 2) / tChange)
        #     prevVal = val
        #     prevTime = time
        # return features

    def __str__(self) -> str:
        """This is a feature for the Mean Squared Displacement of another feature"""
        return "3DMSD"


