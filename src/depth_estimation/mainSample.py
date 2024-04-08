import midasDepthEstimation as mde
import matplotlib.pyplot as plt
import os


# ==========================================================================================
# Example of how to use the module for the depth estimation with an example of file input
# and the output result
# ==========================================================================================

dem = mde.DepthEstimation()

filename = 'street.png'
inputPath = './input/image-source/'
depthEstimatedImage = dem.imageDepth(inputPath + filename)

# Creates the output directory if not already exist
outputPath = './temp-files/'
if not os.path.exists(outputPath):
    os.makedirs(outputPath)

# Save the image with the depth estimation done
outputFileName = outputPath + filename
plt.imsave(fname = outputFileName, arr = depthEstimatedImage)