from typing import List
import glob
import re
import AIfSR_Trajectory_Analysis.Utilities as Utilities

current_working_dir = Utilities.getMainDirectory()

PATH_TO_SIMPLE_CASES = "/data/02_01_Simulated_trajectories/Simple_cases/"
PATH_TO_BALLISTIC_SD = "/data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/"
PATH_TO_BALLISTIC_CD = "/data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/"
PATH_TO_CONFINE_ESC = "/data/02_01_Simulated_trajectories/Confinement_escape/"


def fillFilePaths(filePaths: List[str], pathToCase: str, typeName: str, fullPath: str):
    for file in glob.glob(current_working_dir + pathToCase + typeName + "*.tck"):
        filePaths.append(file)
    for index, txtfile in enumerate(filePaths):
        filePaths[index] = txtfile.replace(current_working_dir + "/", "")
    for i in filePaths:
        i.replace(fullPath, "")
    filePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
    for i in filePaths:
        i = fullPath + i


Ballistic_movementFilePaths = []
Confined_diffusionFilePaths = []
Random_walkFilePaths = []
Very_confined_diffusionFilePaths = []

fillFilePaths(Ballistic_movementFilePaths, PATH_TO_SIMPLE_CASES, "Ballistic_movement/Trajectories/",
              "data/02_01_Simulated_trajectories/Simple_cases/Ballistic_movement/Trajectories/pure_ballistic_")

fillFilePaths(Confined_diffusionFilePaths, PATH_TO_SIMPLE_CASES, "Confined_diffusion/Trajectories/",
              "data/02_01_Simulated_trajectories/Simple_cases/Confined_diffusion/Trajectories/confined_")

fillFilePaths(Random_walkFilePaths, PATH_TO_SIMPLE_CASES, "Random_walk/Trajectories/",
              "data/02_01_Simulated_trajectories/Simple_cases/Random_walk/Trajectories/random_")

fillFilePaths(Very_confined_diffusionFilePaths, PATH_TO_SIMPLE_CASES, "Very_confined_diffusion/Trajectories/",
              "data/02_01_Simulated_trajectories/Simple_cases/Very_confined_diffusion/Trajectories/very_confined_")

Limits_0_1au_Speed_0_001Paths = []
Limits_0_1au_Speed_001_01Paths = []
Limits_0_1au_Speed_0001_001Paths = []
Limits_0_3au_Speed_0_001Paths = []
Limits_0_3au_Speed_001_01Paths = []
Limits_0_3au_Speed_0001_001Paths = []
Limits_0_6au_Speed_0_001Paths = []
Limits_0_6au_Speed_001_01Paths = []
Limits_0_6au_Speed_0001_001Paths = []

fillFilePaths(Limits_0_1au_Speed_0_001Paths, PATH_TO_BALLISTIC_CD, "Limits_0-1au/Speed_0-0.001au/",
              "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/"
              "Speed_0.001-0.01au/ballistic_confined_random_")

fillFilePaths(Limits_0_1au_Speed_001_01Paths, PATH_TO_BALLISTIC_CD, "Limits_0-1au/Speed_0.01-0.1au/",
              "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/"
              "Speed_0.01-0.1au/ballistic_confined_random_")

fillFilePaths(Limits_0_1au_Speed_0001_001Paths, PATH_TO_BALLISTIC_CD, "Limits_0-1au/Speed_0.001-0.01au/",
              "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/"
              "Speed_0.001-0.01au/ballistic_confined_random_")

fillFilePaths(Limits_0_3au_Speed_001_01Paths, PATH_TO_BALLISTIC_CD, "Limits_0-3au/Speed_0.01-0.1au/",
              "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-3au/"
              "Speed_0.01-0.1au/ballistic_confined_random_")

fillFilePaths(Limits_0_3au_Speed_0001_001Paths, PATH_TO_BALLISTIC_CD, "Limits_0-3au/Speed_0.001-0.01au/",
              "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-3au/"
              "Speed_0.001-0.01au/ballistic_confined_random_")

fillFilePaths(Limits_0_6au_Speed_0_001Paths, PATH_TO_BALLISTIC_CD, "Limits_0-6au/Speed_0-0.001au/",
              "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/"
              "Speed_0.001-0.01au/ballistic_confined_random_")

fillFilePaths(Limits_0_6au_Speed_001_01Paths, PATH_TO_BALLISTIC_CD, "Limits_0-6au/Speed_0.01-0.1au/",
              "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/"
              "Speed_0.01-0.1au/ballistic_confined_random_")

fillFilePaths(Limits_0_6au_Speed_0001_001Paths, PATH_TO_BALLISTIC_CD, "Limits_0-6au/Speed_0.001-0.01au/",
              "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/"
              "Speed_0.001-0.01au/ballistic_confined_random_")

Fast_ballisticFilePaths = []
Random_ballisticFilePaths = []
Slow_ballisticFilePaths = []
Confinement_escapeFilePaths = []

fillFilePaths(Fast_ballisticFilePaths, PATH_TO_BALLISTIC_SD, "Fast_ballistic/Trajectories/",
              "data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/"
              "Fast_ballistic/Trajectories/fast_ballistic_simple_")

fillFilePaths(Random_ballisticFilePaths, PATH_TO_BALLISTIC_SD, "Random_ballistic/Trajectories/",
              "data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/"
              "Random_ballistic/Trajectories/ballistic_simple_random_")

fillFilePaths(Slow_ballisticFilePaths, PATH_TO_BALLISTIC_SD, "Slow_ballistic/Trajectories/",
              "data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/"
              "Slow_ballistic/Trajectories/ballistic_simple_")

fillFilePaths(Confinement_escapeFilePaths, PATH_TO_CONFINE_ESC, "Trajectories/",
              "data/02_01_Simulated_trajectories/Confinement_escape/"
              "Trajectories/confinement_escape_")
