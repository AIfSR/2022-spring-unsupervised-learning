from AIfSR_Trajectory_Analysis.features.Features import Features

class FeaturesWithNames (Features):
    def __init__(self, name:str) -> None:
        super().__init__()
        self._name = name

    def getName(self) -> str:
        """Gets the name of these Features"""
        return self._name

    def __eq__(self, o: Features) -> bool:
        return super().__eq__(o) and self._name == o._name

    def __iadd__(self, otherFeature: Features):
        if(type(otherFeature) == FeaturesWithNames and otherFeature._name != self._name):
            raise ValueError()
        return super().__iadd__(otherFeature)