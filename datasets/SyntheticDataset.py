from typing import List, Tuple
from datasets.DatasetBase import DatasetBase
from tckfilereader.Points import Points
import datasets.MzykFilePaths as FP
from tckfilereader.TCKFileReader import TCKFileReader

class SyntheticDataset (DatasetBase):

    def getCategoriesWithPoints(self) -> List[Tuple[str, List[Points]]]:
        """Returns a list of all of the synthetic data split up by the type of 
        diffusion occuring in each trajectory"""
        pass