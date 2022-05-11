The source code for this package is located in src/AIfSR_Trajectory_Analysis.
The test code for this package is located in src/tests.

src/Main.py provides a sample main file to run the predict function from the Trajectory_Analysis file.

Within the src/AIfSR_Trajectory_Analysis directory there are various directories to split up the code. src/tests mimics this structure with test files for each file within src/AIfSR_Trajectory_Analysis.

src/AIfSR_Trajectory_Analysis/algorithmanalysis is a directory containing python notebooks and code to analyze existing algorithms. By running the python notebooks within this directory, information will be printed on how accurate the algorithm was, which trajectories it predicted incorrectly, and some graphs of the trajectories predicted incorrectly.

src/AIfSR_Trajectory_Analysis/algorithms is a directory containing wrapper classes for the various algorithms that can be used. The algorithms all derive from the class AlgorithmBase found within AlgorithmBase.py, so any time a new algorithm is to be created a new file is created in this directory with a class that derives from AlgorithmBase.

src/AIfSR_Trajectory_Analysis/data is a directory containing all of the data necessary to train the algorithms. This data is not tracked on github, so if you are opening this code after cloning it on github you will not have access to this data. This data is stored on google drive, so to gain access either consult the AIfSR team directly, or if you have access to the AIfSR google drive check the folder "For Fall 2022" to find the "data" folder. Download this folder and upload it in place of the data folder listed in src/AIfSR_Trajectory_Analysis. 

src/AIfSR_Trajectory_Analysis/datasetfeatures is a directory containing datasets of already calculated features. The point of this directory is to provide a space to create and access features that have already been calculated from a dataset, so as to save the time of having to recalculate them everytime a new algorithm is to be trained. This is very useful for training algorithms on MSD features, because MSD takes a lot of time to calculate for many trajectories, so this code managaes calculating these values one time, saving them away, and then loading them any time later on when other code needs them.

src/AIfSR_Trajectory_Analysis/datasets is a directory containing the code to access the trajectories directly. This code will find all of the trajectories within the data folder and return back points objects representing each trajectory. These points objects can be used with other code to generate features to be fed into algorithms.

src/AIfSR_Trajectory_Analysis/features is a directory containing the code to extract features from points and other features. Almost all of the files within this directory have classes that derive from the FeatureCreatorBase class found within the FeatureCreatorBase.py file. This means that featureCreators can be be substituted in for one another because they all share the same interface. Almost all of the files within this directory allow for points to be passed into a class, and for a features object to be output representing the features extracted from that points object.

src/AIfSR_Trajectory_Analysis/featurestosingleval contains the code to reduce a set of features down to a single value. This was done to easily compare trajectories to one another. When features were extracted from a trajectory oftentimes it was hard to compare long lists of features across many trajectories. It was much easier to compare single values that represented those long lists of features, so the various files within src/AIfSR_Trajectory_Analysis/featurestosingleval would do that.

src/AIfSR_Trajectory_Analysis/ml_pipelines contains factories that represent the entire pipeline to predict a diffusion type from a trajectory. MLPipelineBase.py has an abstract class MLPipelineBase from which all MLPipelines derive from, and this abstract class provides the interface to get the objects to extract features from a trajectory, normalize those features, standardize the number of those features, and the algorithm that those features should be passed into to predict the type of diffusion occuring.

src/AIfSR_Trajectory_Analysis/normalizefeatures contains code to normalize feature values to be within a certain range. The classes in this directory derive from the base class NormalizeFeaturesBase found within NormalizeFeaturesBase.py.

src/AIfSR_Trajectory_Analysis/output_results contains code to output the results of an algorithm to a usable format. One such way of outputting results would be to an Xlsx file which is done within the OutputXlsx.py file.

src/AIfSR_Trajectory_Analysis/plotting contains the code to plot trajectories and features. There are various strategies and classes for plotting either features, or trajectories, or features represented as single values, and this code all lives within the plotting directory.

src/AIfSR_Trajectory_Analysis/savedgraphs contains python notebooks to plot some useful graphs. Each of the python notebooks within this directory can be run to create graphs that were useful enough that it was deamed important to save them and provide a way to generate them whenever necessary.

src/AIfSR_Trajectory_Analysis/standardizefeaturesnumber contains code to reduce the number of features down to a fixed value. All of the classes within this directory derive from the class StandardizeFeaturesNumberBase found within StandardizeFeaturesNumberBase.py so as to allow for any strategy for standardizing the number of features to be substitued in and out for another.

src/AIfSR_Trajectory_Analysis/tckfilereader contains code to read tck files and output their results as Points objects to be used within the rest of the code base.

src/AIfSR_Trajectory_Analysis/PredictDiffusionTypes.py contains the code used within the predict function in the file: src/AIfSR_Trajectory_Analysis/TrajectoryAnalysis.py. This file exists so as not to clutter up the public interface file: src/AIfSR_Trajectory_Analysis/TrajectoryAnalysis.py

src/AIfSR_Trajectory_Analysis/TrajectoryAnalysis.py contains the public interface code to be used to interact with this python package. This is the only file that needs to be imported in order to use this python pacakage.

src/AIfSR_Trajectory_Analysis/Utilities.py contains commonly needed utility code used throughout the project.