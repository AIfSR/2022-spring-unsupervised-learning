from typing import List
from diffusion_prediction.datasets.MacrophageStageDataset import MacrophageStageDataset
from diffusion_prediction.features.MSDFeatureCreator import MSDFeatureCreator
from diffusion_prediction.features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from diffusion_prediction.plotting.GraphParameters import GraphParameters
from diffusion_prediction.plotting.FeaturesOverIndices import FeaturesOverIndices

from diffusion_prediction.features.XFeatureCreator import XFeatureCreator
from diffusion_prediction.tckfilereader.PointsWithNames import PointsWithNames
from diffusion_prediction.datasets.SyntheticDatasetSubset import SyntheticDatasetSubset
import diffusion_prediction.Utilities as Utilities

plotFeatures = [
        GraphParameters(
            xFeatureCreator=MSDFeatureCreator(XFeatureCreator),
            xLabel = "MSD: X Speed"),
]
realDataset = MacrophageStageDataset()
syntheticDataset = SyntheticDatasetSubset()

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
    def plotTrajectory(categoryNumber:int, trajectoryNumber:int):
        title = syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][trajectoryNumber].title
        FeaturesOverIndices.display_plots(ThreeDMSDFeatureCreator(),
                                        syntheticDataset.getCategoriesWithPoints()[categoryNumber][1][trajectoryNumber],
                                        title=title)
    
    plotTrajectory(0, 0)
    plotTrajectory(1, 44)
    plotTrajectory(2, 39)
    plotTrajectory(3, 43)

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



