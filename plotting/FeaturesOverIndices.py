from typing import Dict, List, Tuple
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.XFeatureCreator import XFeatureCreator
from features.TFeatureCreator import TFeatureCreator
from features.MultiplyByFactorFeatureCreator import MultiplyByFactorFeatureCreator
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from features.MSDFeatureCreator import MSDFeatureCreator
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from tckfilereader.Points import Points
from plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator
from matplotlib.ticker import MaxNLocator


from PIL import Image
from cairosvg import svg2png
from io import BytesIO

class FeaturesOverIndices:

    BOTTOM_CROP = 49
    TOP_CROP = 54
    LEFT_CROP = 76
    RIGHT_CROP = 60

    def display_plots(self, xFeatures:Features, yFeatures:Features, imageFile:str=None, title:str=None, xLabel=None, yLabel=None) -> None:
        """Displays a plot of the yFeatureCreator over time"""

        ax_scatter = plt.axes()

        yLabel = yLabel or ""
        ax_scatter.set_ylabel(yLabel)
        xLabel = xLabel or ""
        ax_scatter.set_xlabel(xLabel)

        if title == None:
            plt.suptitle(self._get_graph_title(yLabel + " vs. " + xLabel))
        else:
            plt.suptitle(title)

        plt.plot(xFeatures, yFeatures, color="red", label="AIfSR")
        plt.legend()

        ax_scatter.set_yscale('log')
        ax_scatter.set_xscale('log')

        ax_scatter.set_zorder(2)
        ax_scatter.set_facecolor('none')

        if imageFile != None:
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
        xFeatures = xFeatures[1:-2]

        
        self.display_plots(xFeatures, yFeatures, imageFile=imageFile, title=title, xLabel="Time Step,s", yLabel=str(yFeatureCreator))



