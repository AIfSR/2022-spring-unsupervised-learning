from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames


class LabeledCategory:
    def __init__(self, name: str, labels: list[float], trajectories: list[PointsWithNames]) -> None:
        self.name = name
        self.labels = labels
        self.trajectories = trajectories
