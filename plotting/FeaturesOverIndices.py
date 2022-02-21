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

    def display_plots(self, yFeatureCreator:FeatureCreatorBase, points:Points) -> None:
        """Displays a plot of the yFeatureCreator over time"""
        #fig = plt.figure(figsize=(16, 7.5))
        
        ax_scatter = plt.axes()
        #ax_scatter.tick_params(direction='in', top=True, right=True)
        
        tFeatureCreator = TFeatureCreator()
        xPoints = tFeatureCreator.get_features(points)
        yPoints = yFeatureCreator.get_features(points)

        xPoints = xPoints[1:len(xPoints)]
        yPoints = yPoints[1:len(yPoints)]
        del xPoints[-2::]
        del yPoints[-2::]
        
        ax_scatter.set_ylabel('MSD, ${\mu}$m${^2}$/s')
        ax_scatter.set_xlabel("Time Step,s")

        plottingNormally = True
        if plottingNormally:
            plt.plot(xPoints, yPoints, color="red")

            #ax_scatter.set_xlim(min(xPoints),max(xPoints))
            #ax_scatter.set_ylim(min(yPoints),max(yPoints))
            ax_scatter.set_yscale('log')
            ax_scatter.set_xscale('log')
            ax_scatter.set_zorder(2)
            ax_scatter.set_facecolor('none')

        usingBackground = True
        if usingBackground:
            ax_tw_x = ax_scatter.twinx()
            ax_tw_x.axis('off')
            ax2 = ax_tw_x.twiny()
            img = svg2png(file_obj=open('image.svg', "rb"))
            im = Image.open(BytesIO(img))
            width, height = im.size
            bottomAdjustment = 63
            top = 49
            left = 77
            rightAdjustment = 60
            print("width: ", width)
            print("height: ", height)
            im = im.crop((left, top, width - rightAdjustment, height - bottomAdjustment))

            ax2.imshow(im, extent=[min(xPoints), max(xPoints), min(yPoints), max(yPoints)], aspect='auto')
            ax2.axis('off')
        
        plt.show()


    def _get_graph_title(self, points:Points, yFeatureCreator:str) -> str:
        """Gets the name of the graph."""
        title = ""

        title += "Time Step vs. " + str(yFeatureCreator) + " comparison"
        return title



