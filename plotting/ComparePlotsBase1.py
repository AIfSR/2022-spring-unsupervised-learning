from abc import ABC, abstractmethod
from typing import List, Tuple

from features.Features import Features
from tckfilereader.Points import Points
from features.FeatureCreatorBase import FeatureCreatorBase


class ComparePlotsBase1 (ABC):

    @abstractmethod
    def display_plots(self, yFeatureCreator:FeatureCreatorBase, points:Points, tile:str=None) -> None:
        """Displays all the plots"""
        pass
