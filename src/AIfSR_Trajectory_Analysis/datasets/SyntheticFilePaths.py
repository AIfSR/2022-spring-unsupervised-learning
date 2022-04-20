import glob
import os
import re
import AIfSR_Trajectory_Analysis.Utilities as Utilities

current_working_dir = Utilities.getMainDirectory()

PATH_TO_SIMPLE_CASES = "/data/02_01_Simulated_trajectories/Simple_cases/"
PATH_TO_BALLISTIC_SD = "/data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/"
PATH_TO_BALLISTIC_CD = "/data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/"
PATH_TO_CONFINE_ESC = "/data/02_01_Simulated_trajectories/Confinement_escape/"

Ballistic_movementFilePaths = []
ballisticPath = current_working_dir + PATH_TO_SIMPLE_CASES + "Ballistic_movement/Trajectories/*.tck"
for file in glob.glob(ballisticPath):
    Ballistic_movementFilePaths.append(file)
for index, txtfile in enumerate(Ballistic_movementFilePaths):
    Ballistic_movementFilePaths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Ballistic_movementFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Simple_cases/Ballistic_movement/Trajectories/pure_ballistic_", "")
Ballistic_movementFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Ballistic_movementFilePaths:
    i = "data/02_01_Simulated_trajectories/Simple_cases/Ballistic_movement/Trajectories/pure_ballistic_" + i

Confined_diffusionFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_SIMPLE_CASES + "Confined_diffusion/Trajectories/*.tck"):
    Confined_diffusionFilePaths.append(file)
for index, txtfile in enumerate(Confined_diffusionFilePaths):
    Confined_diffusionFilePaths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Confined_diffusionFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Simple_cases/Confined_diffusion/Trajectories/confined_", "")
Confined_diffusionFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Confined_diffusionFilePaths:
    i = "data/02_01_Simulated_trajectories/Simple_cases/Confined_diffusion/Trajectories/confined_" + i

Random_walkFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_SIMPLE_CASES + "Random_walk/Trajectories/*.tck"):
    Random_walkFilePaths.append(file)
for index, txtfile in enumerate(Random_walkFilePaths):
    Random_walkFilePaths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Random_walkFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Simple_cases/Random_walk/Trajectories/random_", "")
Random_walkFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Random_walkFilePaths:
    i = "data/02_01_Simulated_trajectories/Simple_cases/Random_walk/Trajectories/random_" + i

Very_confined_diffusionFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_SIMPLE_CASES + "Very_confined_diffusion/Trajectories/*.tck"):
    Very_confined_diffusionFilePaths.append(file)
for index, txtfile in enumerate(Very_confined_diffusionFilePaths):
    Very_confined_diffusionFilePaths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Very_confined_diffusionFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Simple_cases/Very_confined_diffusion/Trajectories/very_confined_", "")
Very_confined_diffusionFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Very_confined_diffusionFilePaths:
    i = "data/02_01_Simulated_trajectories/Simple_cases/Very_confined_diffusion/Trajectories/very_confined_" + i

Limits_0_1au_Speed_0_001Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-1au/Speed_0-0.001au/*.tck"):
    Limits_0_1au_Speed_0_001Paths.append(file)
for index, txtfile in enumerate(Limits_0_1au_Speed_0_001Paths):
    Limits_0_1au_Speed_0_001Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_1au_Speed_0_001Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/"
              "Speed_0.001-0.01au/ballistic_confined_random_", "")
Limits_0_1au_Speed_0_001Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_1au_Speed_0_001Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/" \
        "Speed_0.001-0.01au/ballistic_confined_random_" + i

Limits_0_1au_Speed_001_01Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-1au/Speed_0.01-0.1au/*.tck"):
    Limits_0_1au_Speed_001_01Paths.append(file)
for index, txtfile in enumerate(Limits_0_1au_Speed_001_01Paths):
    Limits_0_1au_Speed_001_01Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_1au_Speed_001_01Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/"
              "Speed_0.01-0.1au/ballistic_confined_random_", "")
Limits_0_1au_Speed_001_01Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_1au_Speed_001_01Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/" \
        "Speed_0.01-0.1au/ballistic_confined_random_" + i

Limits_0_1au_Speed_0001_001Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-1au/Speed_0.001-0.01au/*.tck"):
    Limits_0_1au_Speed_0001_001Paths.append(file)
for index, txtfile in enumerate(Limits_0_1au_Speed_0001_001Paths):
    Limits_0_1au_Speed_0001_001Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_1au_Speed_0001_001Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/"
              "Speed_0.001-0.01au/ballistic_confined_random_", "")
Limits_0_1au_Speed_0001_001Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_1au_Speed_0001_001Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-1au/" \
        "Speed_0.001-0.01au/ballistic_confined_random_" + i

Limits_0_3au_Speed_0_001Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-3au/Speed_0-0.001au/*.tck"):
    Limits_0_3au_Speed_0_001Paths.append(file)
for index, txtfile in enumerate(Limits_0_3au_Speed_0_001Paths):
    Limits_0_3au_Speed_0_001Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_3au_Speed_0_001Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-3au/"
              "Speed_0.001-0.01au/ballistic_confined_random_", "")
Limits_0_3au_Speed_0_001Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_3au_Speed_0_001Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-3au/" \
        "Speed_0.001-0.01au/ballistic_confined_random_" + i

Limits_0_3au_Speed_001_01Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-3au/Speed_0.01-0.1au/*.tck"):
    Limits_0_3au_Speed_001_01Paths.append(file)
for index, txtfile in enumerate(Limits_0_3au_Speed_001_01Paths):
    Limits_0_3au_Speed_001_01Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_3au_Speed_001_01Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-3au/"
              "Speed_0.01-0.1au/ballistic_confined_random_", "")
Limits_0_3au_Speed_001_01Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_3au_Speed_001_01Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-3au/" \
        "Speed_0.01-0.1au/ballistic_confined_random_" + i

Limits_0_3au_Speed_0001_001Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-3au/Speed_0.001-0.01au/*.tck"):
    Limits_0_3au_Speed_0001_001Paths.append(file)
for index, txtfile in enumerate(Limits_0_3au_Speed_0001_001Paths):
    Limits_0_3au_Speed_0001_001Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_3au_Speed_0001_001Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-3au/"
              "Speed_0.001-0.01au/ballistic_confined_random_", "")
Limits_0_3au_Speed_0001_001Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_3au_Speed_0001_001Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-3au/" \
        "Speed_0.001-0.01au/ballistic_confined_random_" + i

Limits_0_6au_Speed_0_001Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-6au/Speed_0-0.001au/*.tck"):
    Limits_0_6au_Speed_0_001Paths.append(file)
for index, txtfile in enumerate(Limits_0_6au_Speed_0_001Paths):
    Limits_0_6au_Speed_0_001Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_6au_Speed_0_001Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/"
              "Speed_0.001-0.01au/ballistic_confined_random_", "")
Limits_0_6au_Speed_0_001Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_6au_Speed_0_001Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/" \
        "Speed_0.001-0.01au/ballistic_confined_random_" + i

Limits_0_6au_Speed_001_01Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-6au/Speed_0.01-0.1au/*.tck"):
    Limits_0_6au_Speed_001_01Paths.append(file)
for index, txtfile in enumerate(Limits_0_6au_Speed_001_01Paths):
    Limits_0_6au_Speed_001_01Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_6au_Speed_001_01Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/"
              "Speed_0.01-0.1au/ballistic_confined_random_", "")
Limits_0_6au_Speed_001_01Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_6au_Speed_001_01Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/" \
        "Speed_0.01-0.1au/ballistic_confined_random_" + i

Limits_0_6au_Speed_0001_001Paths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_CD + "Limits_0-6au/Speed_0.001-0.01au/*.tck"):
    Limits_0_6au_Speed_0001_001Paths.append(file)
for index, txtfile in enumerate(Limits_0_6au_Speed_0001_001Paths):
    Limits_0_6au_Speed_0001_001Paths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Limits_0_6au_Speed_0001_001Paths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/"
              "Speed_0.001-0.01au/ballistic_confined_random_", "")
Limits_0_6au_Speed_0001_001Paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Limits_0_6au_Speed_0001_001Paths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_confined_diffusion/Limits_0-6au/" \
        "Speed_0.001-0.01au/ballistic_confined_random_" + i

Fast_ballisticFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_SD + "Fast_ballistic/Trajectories/*.tck"):
    Fast_ballisticFilePaths.append(file)
for index, txtfile in enumerate(Fast_ballisticFilePaths):
    Fast_ballisticFilePaths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Fast_ballisticFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/"
              "Fast_ballistic/Trajectories/fast_ballistic_simple_", "")
Fast_ballisticFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Fast_ballisticFilePaths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/" \
        "Fast_ballistic/Trajectories/fast_ballistic_simple_" + i

Random_ballisticFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_SD + "Random_ballistic/Trajectories/*.tck"):
    Random_ballisticFilePaths.append(file)
for index, txtfile in enumerate(Random_ballisticFilePaths):
    Random_ballisticFilePaths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Random_ballisticFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/"
              "Random_ballistic/Trajectories/ballistic_simple_random_", "")
Random_ballisticFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Random_ballisticFilePaths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/" \
        "Random_ballistic/Trajectories/ballistic_simple_random_" + i

Slow_ballisticFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_BALLISTIC_SD + "Slow_ballistic/Trajectories/*.tck"):
    Slow_ballisticFilePaths.append(file)
for index, txtfile in enumerate(Slow_ballisticFilePaths):
    Slow_ballisticFilePaths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Slow_ballisticFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/"
              "Slow_ballistic/Trajectories/ballistic_simple_", "")
Slow_ballisticFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Slow_ballisticFilePaths:
    i = "data/02_01_Simulated_trajectories/Ballistic_and_simple_diffusion/" \
        "Slow_ballistic/Trajectories/ballistic_simple_" + i

Confinement_escapeFilePaths = []
for file in glob.glob(current_working_dir + PATH_TO_CONFINE_ESC + "Trajectories/*.tck"):
    Confinement_escapeFilePaths.append(file)
for index, txtfile in enumerate(Confinement_escapeFilePaths):
    Confinement_escapeFilePaths[index] = txtfile.replace(current_working_dir+"/", "")
for i in Confinement_escapeFilePaths:
    i.replace("data/02_01_Simulated_trajectories/Confinement_escape/"
              "Trajectories/confinement_escape_", "")
Confinement_escapeFilePaths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i in Confinement_escapeFilePaths:
    i = "data/02_01_Simulated_trajectories/Confinement_escape/" \
        "Trajectories/confinement_escape_" + i
