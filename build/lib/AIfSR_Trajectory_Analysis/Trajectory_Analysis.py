import AIfSR_Trajectory_Analysis.PredictDiffusionTypes as PredictDiffusionTypes

# predict is the main method that reads in the trajectories, calculates the MSD 
# values for them, predicts their diffusion types, and then prints out these 
# predictions
def predict(inputTrajectoriesDirectory:str):
    # This is the concrete factory class that defines the feature creator, 
    # normalizer, standardizer, and algorithm being used to process the 
    # trajectories for the Logistic Regression algorithm

    PredictDiffusionTypes.checkDirectory(inputTrajectoriesDirectory)

    mlPipeline = PredictDiffusionTypes.LRPipelineFactory()

    algorithm = mlPipeline.getAlgorithm()
    
    points = PredictDiffusionTypes.getTrajectories(inputTrajectoriesDirectory)
    inputFeatures = PredictDiffusionTypes.getFeaturesForAlgorithm(points, mlPipeline)

    predictions = algorithm.predict(inputFeatures)

    PredictDiffusionTypes.printPredictions(predictions)