from typing import Dict, List, Tuple
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from diffusion_prediction.features.FeatureCreatorBase import FeatureCreatorBase
from diffusion_prediction.features.Features import Features
from diffusion_prediction.features.XFeatureCreator import XFeatureCreator
from diffusion_prediction.features.TFeatureCreator import TFeatureCreator
from diffusion_prediction.features.MultiplyByFactorFeatureCreator import MultiplyByFactorFeatureCreator
from diffusion_prediction.features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from diffusion_prediction.features.MSDFeatureCreator import MSDFeatureCreator
from diffusion_prediction.featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from diffusion_prediction.tckfilereader.Points import Points
from matplotlib.ticker import MaxNLocator


from PIL import Image
from cairosvg import svg2png
from io import BytesIO

class IndiciesFeatureCreator (Features):
    def __init__(self, features:Features) -> None:
        super().__init__()
        self._features = features
    
    def get_features(self, points:Points) -> Features:
        features = Features()
        for i in range(len(self._features)):
            features.add_feature_val(i)
        return features
        
class FeaturesOverIndices:

    BOTTOM_CROP = 49
    TOP_CROP = 54
    LEFT_CROP = 76
    RIGHT_CROP = 60
    def display_plot_of_features(self, yFeatures:Features, imageFile:str=None, title:str=None, xLabel:str=None, yLabel:str=None) -> None:
        """Displays a plot of the yFeatureCreator over time"""
        indiciesFeatureCreator = IndiciesFeatureCreator(yFeatures)
        xFeatures = indiciesFeatureCreator.get_features(None)
        self._display_plot_of_features(xFeatures, yFeatures, imageFile, title, xLabel, yLabel)

    def _display_plot_of_features(self, xFeatures:Features, yFeatures:Features, imageFile:str, title:str, xLabel:str, yLabel:str) -> None:
        """Displays a plot of the yFeatureCreator over time"""

        ax_scatter = plt.axes()

        yLabel = yLabel or ""
        ax_scatter.set_ylabel(yLabel)
        xLabel = xLabel or ""
        ax_scatter.set_xlabel(xLabel)

        if title == None:
            plt.suptitle(yLabel + " vs. " + xLabel)
        else:
            plt.suptitle(title)

        ax_scatter.set_yscale('log')
        ax_scatter.set_xscale('log')

        plt.plot(xFeatures, yFeatures, color="red", label="AIfSR")
        plt.legend()

        if imageFile != None:
            ax_scatter.set_zorder(2)
            ax_scatter.set_facecolor('none')
            ax_tw_x = ax_scatter.twinx()
            ax_tw_x.axis('off')
            ax2 = ax_tw_x.twiny()
            img = svg2png(file_obj=open(imageFile, "rb"))
            im = Image.open(BytesIO(img))
            width, height = im.size

            im = im.crop((FeaturesOverIndices.LEFT_CROP, FeaturesOverIndices.TOP_CROP,
                          width - FeaturesOverIndices.RIGHT_CROP, height - FeaturesOverIndices.BOTTOM_CROP))

            ax2.imshow(im, extent=[min(xFeatures), max(xFeatures), min(yFeatures), max(yFeatures)], aspect='auto')
            ax2.axis('off')
        
        plt.show()

    def display_plots(self, yFeatureCreator:FeatureCreatorBase, points:Points, imageFile:str=None, title:str=None) -> None:
        tFeatureCreator = MultiplyByFactorFeatureCreator(TFeatureCreator(), 1 / 1000)
        xFeatures = tFeatureCreator.get_features(points)
        yFeatures = yFeatureCreator.get_features(points)
        xFeatures = xFeatures[:len(yFeatures)]

        self._display_plot_of_features(xFeatures, yFeatures, imageFile, title, "Time Step,s", str(yFeatureCreator))



