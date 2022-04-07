from abc import ABC, abstractmethod
from typing import List, Tuple

from diffusion_prediction.tckfilereader.Points import Points

class DatasetBase(ABC):

    @abstractmethod
    def getCategoriesWithPoints(self) -> List[Tuple[str, List[Points]]]:
        """Returns a list of tuples where each entry is a category name 
        and the list of points that correspond with that category"""
        pass
