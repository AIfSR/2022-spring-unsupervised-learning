from AIfSR_Trajectory_Analysis.features.Features import Features

class FeaturesWithNames (Features):
    def __init__(self, name:str) -> None:
        super().__init__()
        self._name = name

    def getName(self) -> str:
        """Gets the name of these Features"""
        return self._name

    