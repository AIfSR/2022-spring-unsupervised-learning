import glob
import os
import re


current_working_dir = os.getcwd()
path = os.path.dirname(os.path.abspath(__file__))

current_working_dir = current_working_dir.replace('datasets','')

PATH_TO_SIMPLE_CASES = "/data/02_01_Simulated_trajectories/Simple_cases/"

Ballistic_movementFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_SIMPLE_CASES + "Ballistic_movement/trajectories/*.tck"):
    Ballistic_movementFilePaths.append(file)
for index, txtfile in enumerate(Ballistic_movementFilePaths):
        Ballistic_movementFilePaths[index] = txtfile.replace(current_working_dir+"/","")
for i in Ballistic_movementFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Simple_cases/Ballistic_movement/trajectories/pure_ballistic_","")
Ballistic_movementFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Ballistic_movementFilePaths:
    i = "data/02_01_Simulated_trajectories/Simple_cases/Ballistic_movement/trajectories/pure_ballistic_" + i


Confined_diffusionFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_SIMPLE_CASES + "Confined_diffusion/trajectories/*.tck"):
    Confined_diffusionFilePaths.append(file)
for index, txtfile in enumerate(Confined_diffusionFilePaths):
        Confined_diffusionFilePaths[index] = txtfile.replace(current_working_dir+"/","")
for i in Confined_diffusionFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Simple_cases/Confined_diffusion/trajectories/confined_","")
Confined_diffusionFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Confined_diffusionFilePaths:
    i = "data/02_01_Simulated_trajectories/Simple_cases/Confined_diffusion/trajectories/confined_" + i


Random_walkFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_SIMPLE_CASES + "Random_walk/trajectories/*.tck"):
    Random_walkFilePaths.append(file)
for index, txtfile in enumerate(Random_walkFilePaths):
        Random_walkFilePaths[index] = txtfile.replace(current_working_dir+"/","")
for i in Random_walkFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Simple_cases/Random_walk/trajectories/random_","")
Random_walkFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Random_walkFilePaths:
    i = "data/02_01_Simulated_trajectories/Simple_cases/Random_walk/trajectories/random_" + i




Very_confined_diffusionFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_SIMPLE_CASES + "Very_confined_diffusion/trajectories/*.tck"):
    Very_confined_diffusionFilePaths.append(file)
for index, txtfile in enumerate(Very_confined_diffusionFilePaths):
        Very_confined_diffusionFilePaths[index] = txtfile.replace(current_working_dir+"/","")
for i in Very_confined_diffusionFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Simple_cases/Very_confined_diffusion/trajectories/very_confined_","")
Very_confined_diffusionFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Very_confined_diffusionFilePaths:
    i = "data/02_01_Simulated_trajectories/Simple_cases/Very_confined_diffusion/trajectories/very_confined_" + i

