from abc import ABC, abstractmethod
from typing import List, Tuple

from AIfSR_Trajectory_Analysis.features.Features import Features
from AIfSR_Trajectory_Analysis.plotting.GraphParameters import GraphParameters
from AIfSR_Trajectory_Analysis.tckfilereader.Points import Points


class ComparePlotsBase (ABC):

    @abstractmethod
    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays all the plots"""
        pass
