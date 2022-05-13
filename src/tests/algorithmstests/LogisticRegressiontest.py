import unittest
from AIfSR_Trajectory_Analysis.algorithms.LogisticRegression import LogisticRegression
from AIfSR_Trajectory_Analysis.datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures


class LogisticRegressionTest(unittest.TestCase):

    def test_predict(self):
        syntheticMSDFeatures = SyntheticMSDFeatures()
        loaded_labels = syntheticMSDFeatures.getLabels()
        loaded_dataSet = syntheticMSDFeatures.getDatasetOfFeatures()
        dataset = loaded_dataSet[:10] + loaded_dataSet[1510:1520] + loaded_dataSet[3010:3020] + loaded_dataSet[4510:4520]
        labels = loaded_labels[:10] + loaded_labels[1510:1520] + loaded_labels[3010:3020] + loaded_labels[4510:4520]
        extractedLabels = []
        for i in labels:
            extractedLabels.append(i[0]) 
        algorithm = LogisticRegression("BAL")
        algorithm.train(dataset, extractedLabels)
        result = list(algorithm.predict(loaded_dataSet[:1]))
        self.assertEqual(result, [1.0])
