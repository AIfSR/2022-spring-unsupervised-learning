from AIfSR_Trajectory_Analysis.Trajectory_Analysis import predict
from typing import Tuple
import sys

def getUserArguments() -> Tuple[str,str,str]:
    """Ensures that the arguments passed into the python call are correct and 
    then returns them"""
    if(len(sys.argv) != 4):
        sys.exit("Pass three arguments to Main.py, first being the directory name, second being the name of the Excel"
                 "file, third being the name of the spreadsheet")
    directory = sys.argv[1]
    excelFile = sys.argv[2]
    sheetName = sys.argv[3]
    return directory, excelFile, sheetName

if __name__ == "__main__":
    inputTrajectoriesDirectory, excelFile, sheetName = getUserArguments()
    predict(inputTrajectoriesDirectory, excelFile, sheetName)

    # predict(inputTrajectoriesDirectory, "/Users/seandoyle/Downloads/TestSheet.xlsx")
