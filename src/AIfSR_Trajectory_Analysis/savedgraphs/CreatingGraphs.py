from typing import List
from AIfSR_Trajectory_Analysis.datasets.MacrophageStageDataset import MacrophageStageDataset
from AIfSR_Trajectory_Analysis.features.MSDFeatureCreator import MSDFeatureCreator
from AIfSR_Trajectory_Analysis.features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from AIfSR_Trajectory_Analysis.plotting.GraphParameters import GraphParameters
from AIfSR_Trajectory_Analysis.plotting.FeaturesOverIndices import FeaturesOverIndices

from AIfSR_Trajectory_Analysis.features.XFeatureCreator import XFeatureCreator
from AIfSR_Trajectory_Analysis.tckfilereader.PointsWithNames import PointsWithNames
from AIfSR_Trajectory_Analysis.datasets.SyntheticDataset import SyntheticDataset
import AIfSR_Trajectory_Analysis.Utilities as Utilities

plotFeatures = [
        GraphParameters(
            xFeatureCreator=MSDFeatureCreator(XFeatureCreator),
            xLabel = "MSD: X Speed"),
]
realDataset = MacrophageStageDataset()
syntheticDataset = SyntheticDataset()

FeaturesOverIndices = FeaturesOverIndices()

def getPicturePathway(diffusionType:str, pointsWithNames:PointsWithNames):
    imagePath = Utilities.getMainDirectory() + "/data/02_01_Simulated_trajectories/Simple_cases/"
    fullFileName = pointsWithNames.title
    fileName = fullFileName.split("/")[-1]
    underscores = 0
    for i in range(len(fileName)-1):
        if fileName[i] == "_":
            underscores += 1
            if underscores == 2:
                fileName = fileName[:i] + fileName[i+1:]

    if diffusionType == "Bal":
        imagePath += "Ballistic_movement/Figures/MSDs " + fileName + " .svg"
    elif diffusionType == "CD":
        imagePath += "Confined_diffusion/Figures/MSDs " + fileName + " .svg"
    elif diffusionType == "RW":
        imagePath += "Random_walk/Figures/MSDs " + fileName + " .svg"
    else:
        imagePath += "Very_confined_diffusion/Figures/MSDs " + fileName + " .svg"
    return imagePath

def createGraphsOfSampleOfSyntheticDataset():
    def plotTrajectory(categoryNumber:int, categories):
        title = categories[categoryNumber][1][0].title
        FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                        categories[categoryNumber][1][0],
                                        title=title)
    
    categories = syntheticDataset.getCategoriesWithPoints(5)
    plotTrajectory(0, categories)
    plotTrajectory(1, categories)
    plotTrajectory(2, categories)
    plotTrajectory(3, categories)

def createGraphsOfSyntheticDataset():
    i = 0;
    j = 0;
    k = 0;

    for i in range(len(syntheticDataset.getCategoriesWithPoints())):
        for k in range(len(syntheticDataset.getCategoriesWithPoints()[i][1])):
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              syntheticDataset.getCategoriesWithPoints()[i][1][k],
                                              title=syntheticDataset.getCategoriesWithPoints()[i][1][k].title)

def createGraphsOfRealDataset():
    i = 0;
    j = 0;
    k = 0;
    for i in range(len(realDataset.getCategoriesWithPoints())):
        for k in range(len(realDataset.getCategoriesWithPoints()[i][1])):
            FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                              realDataset.getCategoriesWithPoints()[i][1][k],
                                              title=realDataset.getCategoriesWithPoints()[i][1][k].title)

def createGraphsOfSampleOfRealDataset():
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                      realDataset.getCategoriesWithPoints()[0][1][1],
                                      title=realDataset.getCategoriesWithPoints()[0][1][1].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                      realDataset.getCategoriesWithPoints()[0][1][6],
                                      title=realDataset.getCategoriesWithPoints()[0][1][6].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[0][1][13],
                                          title=realDataset.getCategoriesWithPoints()[0][1][13].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][4],
                                          title=realDataset.getCategoriesWithPoints()[1][1][4].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][8],
                                          title=realDataset.getCategoriesWithPoints()[1][1][8].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][11],
                                          title=realDataset.getCategoriesWithPoints()[1][1][11].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[1][1][16],
                                          title=realDataset.getCategoriesWithPoints()[1][1][16].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][2],
                                          title=realDataset.getCategoriesWithPoints()[2][1][2].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][10],
                                          title=realDataset.getCategoriesWithPoints()[2][1][10].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][14],
                                          title=realDataset.getCategoriesWithPoints()[2][1][14].title)
    FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                          realDataset.getCategoriesWithPoints()[2][1][18],
                                          title=realDataset.getCategoriesWithPoints()[2][1][18].title)



