

class FeatureStandardizationError (Exception):
    def __str__(self) -> str:
        return super().__str__() + "Problem Standardizing Feature"