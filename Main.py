
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from normalizefeatures.DoNothingNormalization import DoNothingNormalization
from features.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator

from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval

if __name__ == "__main__":

    dataset = SyntheticDataset()
    categories = dataset.getCategoriesWithPoints()

    normalizeFeatures = DoNothingNormalization()
    standardizeFeatures = Extract40ValsRegularInterval()
    featureCreator = ThreeDMSDFeatureCreator()

    trainingSet = []
    labels = []
    numOfLabels = len(categories)
    for i in range(len(categories)):
        for example in categories[1]:
            trainingSet.append(featureCreator.get_features(example))
            label = [0] * numOfLabels
            label[i] = 1
            labels.append(label)

    trainingSet = normalizeFeatures.normalizeToSetOfFeatures(trainingSet)
    trainingSet = standardizeFeatures.standardizeSetOfFeatures(trainingSet)

    # Algo code here

