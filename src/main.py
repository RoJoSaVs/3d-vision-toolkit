import depth_estimation_module.depthEstimator as dem
import matplotlib.pyplot as plt
import os


# ==========================================================================================
# Example of how to use the module for the depth estimation with an example of file input
# and the output result
# ==========================================================================================


fileName = 'street.png'
inputPath = './image-source/'
depthEstimatedImage = dem.depthImageEstimation(inputPath + fileName)


# Creates the output directory if not already exist
outputPath = './depth-estimation-images/'
if not os.path.exists(outputPath):
    os.makedirs(outputPath)


outputFileName = outputPath + fileName
plt.imsave(fname = outputFileName, arr = depthEstimatedImage)