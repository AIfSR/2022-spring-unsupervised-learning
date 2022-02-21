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

class FeaturesOverIndices(ComparePlotsBase1):

    def display_plots(self, yFeatureCreator:FeatureCreatorBase, points:Points, title:str=None) -> None:
        """Displays plots comparing single point values of a feature for each category"""
        # plt.close()
        fig = plt.figure(figsize=(16, 7.5))
        ax_scatter = plt.axes()
        ax_scatter.tick_params(direction='in', top=True, right=True)
        pointsPlotted = []
        # xPoints= []
        tFeatureCreator = TFeatureCreator()
        xPoints = tFeatureCreator.get_features(points)
        yPoints = yFeatureCreator.get_features(points)
        del xPoints._featuresList[-2::]
        del yPoints._featuresList[-2::]
        # y = 0
        # while (y < len(yPoints)):
        #     xPoints.append(y)
        #     y = y+1
        # del xPoints[0]
        # s = ax_scatter.scatter(xPoints, yPoints)
        # pointsPlotted.append((xPoints, yPoints, s.get_ec()))
        ax_scatter.set_ylabel('MSD, ${\mu}$m${^2}$/s')
        ax_scatter.set_xlabel("Time Step,s")
        # plt.plot(xPoints, yPoints, '--b')
        plt.plot(xPoints[1:len(xPoints)], yPoints[1:len(xPoints)],'--b')

        plt.xscale('log')
        plt.yscale('log')
        if title == None:
            fig.suptitle(self._get_graph_title(points,yFeatureCreator))
        else:
            fig.suptitle(title)
        plt.show()


    def _get_graph_title(self, points:Points, yFeatureCreator:str) -> str:
        """Gets the name of the graph."""
        title = ""
        # title += category[0] + ", "

        title += "Time Step vs. " + str(yFeatureCreator) + " comparison"
        return title



