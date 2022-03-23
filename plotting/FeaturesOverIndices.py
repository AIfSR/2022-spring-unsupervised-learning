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

from PIL import Image
from cairosvg import svg2png
from io import BytesIO

class FeaturesOverIndices:

    BOTTOM_CROP = 49
    TOP_CROP = 54
    LEFT_CROP = 76
    RIGHT_CROP = 60

    def display_plots(self, yFeatureCreator:FeatureCreatorBase, points:Points, imageFile:str, title:str=None) -> None:
        """Displays a plot of the yFeatureCreator over time"""
        
        ax_scatter = plt.axes()
        
        tFeatureCreator = MultiplyByFactorFeatureCreator(TFeatureCreator(), 1/1000)
        xPoints = tFeatureCreator.get_features(points)
        yPoints = yFeatureCreator.get_features(points)

        xPoints = xPoints[1:-2]
        ax_scatter.set_ylabel(str(yFeatureCreator))
        ax_scatter.set_xlabel("Time Step,s")

        plottingNormally = True
        if title == None:
            plt.suptitle(self._get_graph_title(yFeatureCreator))
        else:
            plt.suptitle(title)

        if plottingNormally:
            plt.plot(xPoints, yPoints, color="red", label = "AIfSR")
            plt.legend()
            
            ax_scatter.set_yscale('log')
            ax_scatter.set_xscale('log')
        
            ax_scatter.set_zorder(2)
            ax_scatter.set_facecolor('none')

        usingBackground = False
        if usingBackground:
            ax_tw_x = ax_scatter.twinx()
            ax_tw_x.axis('off')
            ax2 = ax_tw_x.twiny()
            img = svg2png(file_obj=open(imageFile, "rb"))
            im = Image.open(BytesIO(img))
            width, height = im.size
            
            im = im.crop((FeaturesOverIndices.LEFT_CROP, FeaturesOverIndices.TOP_CROP, width - FeaturesOverIndices.RIGHT_CROP, height - FeaturesOverIndices.BOTTOM_CROP))

            ax2.imshow(im, extent=[min(xPoints), max(xPoints), min(yPoints), max(yPoints)], aspect='auto')
            ax2.axis('off')

        plt.show()


    def _get_graph_title(self, yFeatureCreator:str) -> str:
        """Gets the name of the graph."""
        title = ""

        title += "Time Step vs. " + str(yFeatureCreator) + " comparison"
        return title



