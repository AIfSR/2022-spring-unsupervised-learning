This package was designed to analyze the trajectories of nanodiamonds in macrophages. Machine learning algorithms were trained on synthetic datasets to predict the type of diffusion occuring within a trajectory based on the path of the trajectory alone. 
To install this package run the command:
pip install <PATH_TO_DIRECTORY_CONTAINING_setup.cfg>
The public interface from which this package is intended to be used is the file Trajectory_Analysis.py. Within this file, the "predict" function takes in a directory and will print out the results of predicting the diffusion types of all of the trajectories within that directory.
