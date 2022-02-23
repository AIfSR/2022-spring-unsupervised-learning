from typing import Dict, List, Tuple
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.XFeatureCreator import XFeatureCreator
from features.TFeatureCreator import TFeatureCreator
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from features.MSDFeatureCreator import MSDFeatureCreator
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from plotting.ComparePlotsBase1 import ComparePlotsBase1
from tckfilereader.Points import Points
from plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator

from PIL import Image
from cairosvg import svg2png
from io import BytesIO

class FeaturesOverIndices(ComparePlotsBase1):

    BOTTOM_CROP = 63
    TOP_CROP = 49
    LEFT_CROP = 77
    RIGHT_CROP = 60

    def display_plots(self, yFeatureCreator:FeatureCreatorBase, points:Points, imageFile:str) -> None:
        """Displays a plot of the yFeatureCreator over time"""
        
        ax_scatter = plt.axes()
        
        tFeatureCreator = TFeatureCreator()
        xPoints = tFeatureCreator.get_features(points)
        yPoints = yFeatureCreator.get_features(points)

        # This code is here, because the first and last two points are removed
        # from Alina's plotting software
        xPoints = xPoints[1:len(xPoints)]
        yPoints = yPoints[1:len(yPoints)]
        del xPoints[-2::]
        del yPoints[-2::]
        
        ax_scatter.set_ylabel('MSD, ${\mu}$m${^2}$/s')
        ax_scatter.set_xlabel("Time Step,s")

        plottingNormally = True
        if plottingNormally:
            plt.plot(xPoints, yPoints, color="red")

            ax_scatter.set_yscale('log')
            ax_scatter.set_xscale('log')
            ax_scatter.set_zorder(2)
            ax_scatter.set_facecolor('none')

        usingBackground = True
        if usingBackground:
            ax_tw_x = ax_scatter.twinx()
            ax_tw_x.axis('off')
            ax2 = ax_tw_x.twiny()
            img = svg2png(file_obj=open(imageFile, "rb"))
            im = Image.open(BytesIO(img))
            width, height = im.size
            
            print("width: ", width)
            print("height: ", height)
            im = im.crop((FeaturesOverIndices.LEFT_CROP, FeaturesOverIndices.TOP_CROP, width - FeaturesOverIndices.RIGHT_CROP, height - FeaturesOverIndices.BOTTOM_CROP))

            ax2.imshow(im, extent=[min(xPoints), max(xPoints), min(yPoints), max(yPoints)], aspect='auto')
            ax2.axis('off')
        
        plt.show()


    def _get_graph_title(self, points:Points, yFeatureCreator:str) -> str:
        """Gets the name of the graph."""
        title = ""

        title += "Time Step vs. " + str(yFeatureCreator) + " comparison"
        return title



