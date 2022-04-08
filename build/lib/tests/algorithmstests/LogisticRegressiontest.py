import unittest
from diffusion_prediction.algorithms.LogisticRegression import LogisticRegression
from diffusion_prediction.datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures


class LogisticRegressionTest(unittest.TestCase):

    def test_predict(self):
        assert False
        syntheticMSDFeatures = SyntheticMSDFeatures()
        loaded_labels = syntheticMSDFeatures.getLabels()
        loaded_dataSet = syntheticMSDFeatures.getDatasetOfFeatures()
        dataset = loaded_dataSet[:10] + loaded_dataSet[1510:1520] + loaded_dataSet[3010:3020] + loaded_dataSet[4510:4520]
        labels = loaded_labels[:10] + loaded_labels[1510:1520] + loaded_labels[3010:3020] + loaded_labels[4510:4520]

        algorithm = LogisticRegression()
        algorithm.train(dataset, labels)
        result = list(algorithm.predict(loaded_dataSet[:10]))
        self.assertEqual(result, [1,1,1,1,1,1,1,1,1,1])



