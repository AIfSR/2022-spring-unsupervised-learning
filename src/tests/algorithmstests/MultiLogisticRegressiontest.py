import unittest
from AIfSR_Trajectory_Analysis.algorithms.MultiLogisticRegression import MultiLogisticRegression
from AIfSR_Trajectory_Analysis.datasetfeatures.SyntheticMSDFeatures import SyntheticMSDFeatures


class MultiLogisticRegressionTest(unittest.TestCase):

    def test_predict(self):
        syntheticMSDFeatures = SyntheticMSDFeatures()
        loaded_labels = syntheticMSDFeatures.getLabels()
        loaded_dataSet = syntheticMSDFeatures.getDatasetOfFeatures()
        dataset = loaded_dataSet[:10] + loaded_dataSet[1510:1520] + loaded_dataSet[3010:3020] + loaded_dataSet[4510:4520]
        labels = loaded_labels[:10] + loaded_labels[1510:1520] + loaded_labels[3010:3020] + loaded_labels[4510:4520]

        algorithm = MultiLogisticRegression()
        algorithm.train(dataset, labels)
        result = list(algorithm.predict(loaded_dataSet[:1]))
        self.assertEqual(result, [('data/02_01_Simulated_trajectories/Simple_cases/Ballistic_movement/Trajectories/'
                                   'pure_ballistic_0.tck', [1.0, 0.0, 0.0])])
