import AIfSR_Trajectory_Analysis.PredictDiffusionTypes as PredictDiffusionTypes

def predict(inputTrajectoriesDirectory:str):
    """This is the function used to predict the diffusion types of trajectories 
    using the most accurate machine learning model within this build. Pass in 
    the path to a directory as a string and every trajectory within that 
    directory will be analyzed. Trajectories are files that end in .tck and 
    contain x,y,z,t points in the following format:
    line 1: x points, seperated by spaces
    line 2: y points, seperated by spaces
    line 3: z points, seperated by spaces
    line 4: t points, seperated by spaces
    This function will print out the file names of the trajectories it predicts 
    and then the type(s) of diffusion that it detects within those trajectories

    Example usage (Assume /Users/seandoyle/MyDirectory is a directory containing 
    the trajectories: Trajectory1.tck, Trajectory2.tck, and Trajectory3.tck):
    >>> predict("/Users/seandoyle/MyDirectory")
    /Users/seandoyle/MyDirectory/Trajectory1.tck:
    Ballistic: No, Confined Diffusion: No, Random Walk: Yes, Very Confined Diffusion: No

    /Users/seandoyle/MyDirectory/Trajectory2.tck:
    Ballistic: No, Confined Diffusion: No, Random Walk: No, Very Confined Diffusion: Yes

    /Users/seandoyle/MyDirectory/Trajectory3.tck:
    Ballistic: No, Confined Diffusion: Yes, Random Walk: No, Very Confined Diffusion: No
    """
    PredictDiffusionTypes.checkDirectory(inputTrajectoriesDirectory)

    mlPipeline = PredictDiffusionTypes.LRPipelineFactory()

    algorithm = mlPipeline.getAlgorithm()
    
    points = PredictDiffusionTypes.getTrajectories(inputTrajectoriesDirectory)
    inputFeatures = PredictDiffusionTypes.getFeaturesForAlgorithm(points, mlPipeline)

    predictions = algorithm.predict(inputFeatures)

    PredictDiffusionTypes.printPredictions(predictions)