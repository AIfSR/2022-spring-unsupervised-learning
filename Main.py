
from datasets.SyntheticDatasetSubset import SyntheticDatasetSubset
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from normalizefeatures.DoNothingNormalization import DoNothingNormalization

from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval

if __name__ == "__main__":

    dataset = SyntheticDatasetSubset()
    categories = dataset.getCategoriesWithPoints()
    normalizeFeatures = DoNothingNormalization()
    standardizeFeatures = Extract40ValsRegularInterval()
    featureCreator = ThreeDMSDFeatureCreator()

    trainingSet = []
    labels = []
    for i in range(len(categories)):
        for example in categories[1]:
            trainingSet.append(featureCreator.get_features(example))

    trainingSet = normalizeFeatures.normalizeToSetOfFeatures(trainingSet)
    trainingSet = standardizeFeatures.standardizeSetOfFeatures(trainingSet)

    # Algo code here
    



