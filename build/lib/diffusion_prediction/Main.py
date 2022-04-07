from diffusion_prediction.PredictDiffusionTypes import predict
import sys

def getUserArguments() -> str:
    """Ensures that the arguments passed into the python call are correct and 
    then returns them"""
    if(len(sys.argv) != 2):
        sys.exit("Pass a single argument to Main.py that is the directory of the trajectories to be analyzed.")
    directory = sys.argv[1]
    return directory

if __name__ == "__main__":
    inputTrajectoriesDirectory = getUserArguments()
    predict(inputTrajectoriesDirectory)
    
