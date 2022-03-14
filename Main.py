
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from normalizefeatures.DoNothingNormalization import DoNothingNormalization
from datasets.SyntheticDatasetSubset import SyntheticDatasetSubset
from algorithms.LogisticRegression import LogisticRegression

from standardizefeaturesnumber.Extract40ValsRegularInterval import Extract40ValsRegularInterval


if __name__ == "__main__":

    dataset = SyntheticDatasetSubset()
    categories = dataset.getCategoriesWithPoints()

    normalizeFeatures = DoNothingNormalization()
    standardizeFeatures = Extract40ValsRegularInterval()
    featureCreator = ThreeDMSDFeatureCreator()
    print("Here")
    algorithm = LogisticRegression()

    trainingSet = []
    labels = []
    numOfLabels = len(categories)

    count = 0
    for i in range(len(categories)):
        for example in categories[i][1]:
            trainingSet.append(featureCreator.get_features(example))
            label = [0] * numOfLabels
            label[i] = 1
            labels.append(label)
            print(count)
            count += 1

    trainingSet = normalizeFeatures.normalizeToSetOfFeatures(trainingSet)
    trainingSet = standardizeFeatures.standardizeSetOfFeatures(trainingSet)

    print("Here")
    algorithm.train(trainingSet, labels)

