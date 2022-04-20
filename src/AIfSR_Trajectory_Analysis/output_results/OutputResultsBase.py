from abc import ABC, abstractmethod

class OutputResultsBase (ABC):

    @abstractmethod
    def output(self, results:list[tuple[str, list[float], list[float]]]):
        pass