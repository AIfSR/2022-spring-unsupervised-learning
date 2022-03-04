import glob
import os
import re


current_working_dir = os.getcwd()
path = os.path.dirname(os.path.abspath(__file__))

current_working_dir = current_working_dir.replace('datasets','')

Ballistic_movementFilePaths = []
for file in glob.glob(current_working_dir + "/data/Simple_cases/Ballistic_movement/trajectories/*.tck"):
    Ballistic_movementFilePaths.append(file)
for index, txtfile in enumerate(Ballistic_movementFilePaths):
        Ballistic_movementFilePaths[index] = txtfile.replace(current_working_dir+"/","")
Ballistic_movementFilePaths.sort(key=lambda test_string : list(
    map(int, re.findall(r'\d+', test_string)))[0])


Confined_diffusionFilePaths = []
for file in glob.glob(current_working_dir +"/data/Simple_cases/Confined_diffusion/trajectories/*.tck"):
    Confined_diffusionFilePaths.append(file)
for index, txtfile in enumerate(Confined_diffusionFilePaths):
        Confined_diffusionFilePaths[index] = txtfile.replace(current_working_dir+"/","")
Confined_diffusionFilePaths.sort(key=lambda test_string : list(
    map(int, re.findall(r'\d+', test_string)))[0])


Random_walkFilePaths = []
for file in glob.glob(current_working_dir +"/data/Simple_cases/Random_walk/trajectories/*.tck"):
    Random_walkFilePaths.append(file)
for index, txtfile in enumerate(Random_walkFilePaths):
        Random_walkFilePaths[index] = txtfile.replace(current_working_dir+"/","")
Random_walkFilePaths.sort(key=lambda test_string : list(
    map(int, re.findall(r'\d+', test_string)))[0])


Very_confined_diffusionFilePaths = []
for file in glob.glob(current_working_dir +"/data/Simple_cases/Very_confined_diffusion/trajectories/*.tck"):
    Very_confined_diffusionFilePaths.append(file)
for index, txtfile in enumerate(Very_confined_diffusionFilePaths):
        Very_confined_diffusionFilePaths[index] = txtfile.replace(current_working_dir+"/","")
Very_confined_diffusionFilePaths.sort(key=lambda test_string : list(
    map(int, re.findall(r'\d+', test_string)))[0])

