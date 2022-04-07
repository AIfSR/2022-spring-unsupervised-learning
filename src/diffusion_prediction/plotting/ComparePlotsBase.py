from abc import ABC, abstractmethod
from typing import List, Tuple

from diffusion_prediction.features.Features import Features
from diffusion_prediction.plotting.GraphParameters import GraphParameters
from diffusion_prediction.tckfilereader.Points import Points


class ComparePlotsBase (ABC):

    @abstractmethod
    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays all the plots"""
        pass
