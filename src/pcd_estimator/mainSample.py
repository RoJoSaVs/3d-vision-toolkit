import sys
import numpy as np

# Local imports
import pcdEstimator as pcdE
sys.path.append('./src')
import image_handler.imageIO as imageIO
import pcd_handler.pcdFileHandler as pcdFileHandler


filename = 'street.png'

# Load the original image
imageSourcePath = './input/image-source/'
streetOriginal = imageIO.readImage(imageSourcePath + filename)

# Load the depth estimated image
depthImagesPath = './temp-files/depth-estimation-images/'
streetDepth = imageIO.readImage(depthImagesPath + filename)

# Converts the image to grayscale
streetG = imageIO.imageToGrayScale(streetDepth)

# Creates the array with the depth using [x, y, z, rgb]
positionCalculatorResult = pcdE.positionCalculator(streetOriginal, streetG)

# # Turns the result to a numpy array of: [1 Row] [N columns] [4 numbers each column (x, y, z, rgb)]
numpyArrayResult = np.asarray(positionCalculatorResult)

# # Stores the numpy array as a pcd file
filename = './output/pcd-files/test.pcd'
pcdFileHandler.pcdFileGenerator(numpyArrayResult, filename)
