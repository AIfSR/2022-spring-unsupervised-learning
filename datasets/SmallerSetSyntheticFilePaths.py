import glob
import os
import re


current_working_dir = os.getcwd()
path = os.path.dirname(os.path.abspath(__file__))

current_working_dir = current_working_dir.replace('datasets','')

PATH_TO_SIMPLE_CASES = "/data/02_01_Simulated_trajectories/Simple_cases/"
NUMBER_OF_FILES = 50

def getFiles(numberOfFiles:int, path:str, ) -> list[str]:
    files = []
    count = 0
    for file in glob.glob(current_working_dir + path):
        files.append(file)
        count += 1
        if count >= numberOfFiles:
            break
    for index, txtfile in enumerate(files):
            files[index] = txtfile.replace(current_working_dir+"/","")
    files.sort(key=lambda test_string : list(
        map(int, re.findall(r'\d+', test_string)))[0])
    return files

Ballistic_movementFilePaths = getFiles(NUMBER_OF_FILES, PATH_TO_SIMPLE_CASES + "Ballistic_movement/trajectories/*.tck")
Confined_diffusionFilePaths = getFiles(NUMBER_OF_FILES, PATH_TO_SIMPLE_CASES + "Confined_diffusion/trajectories/*.tck")
Random_walkFilePaths = getFiles(NUMBER_OF_FILES, PATH_TO_SIMPLE_CASES + "Random_walk/trajectories/*.tck")
Very_confined_diffusionFilePaths = getFiles(NUMBER_OF_FILES, PATH_TO_SIMPLE_CASES + "Very_confined_diffusion/trajectories/*.tck")

