import sys
import numpy as np

# Add 'src/cli' directory to sys.path to use import inside different files
sys.path.append('src/cli/')


import depth_estimation.midasDepthEstimation as midasDepthEstimation
import image_handler.imageIO as imageIO
import pcd_estimator.pcdEstimator as pcdEstimator
import pcd_handler.pcdFileHandler as pcdFileHandler
import cli.commandLineInterface as CLI
import cli.constants as CONST


# @brief This method call the functions needed to create the point cloud data file based on an input image
# @param fileName: Name of the file that will be processed
# @param filePathSource: Full folder path where the file exist
# @return If the process has finished returns True otherwise false
def processImage(fileName, filePathSource):
    try:
        depthInstance = midasDepthEstimation.DepthEstimation()
        resultImageDepth = depthInstance.imageDepth(filePathSource)
        CLI.showInfoMessage('Image depth estimation was performed')

        tempFolder = CONST.TEMP_FOLDER + fileName
        imageIO.writeImage(tempFolder, resultImageDepth)
        CLI.showInfoMessage('The resulting depth estimation image can be found in the folder: ' + tempFolder)

        originalImage = imageIO.readImage(filePathSource)
        depthImage = imageIO.readImage(tempFolder)
        grayScaleImageAsNumpy = imageIO.imageToGrayScale(depthImage)
        CLI.showInfoMessage('Loading the image to realize the transformation to a 3D file')

        pcdArray = pcdEstimator.positionCalculator(originalImage, grayScaleImageAsNumpy)
        pcdNumpyArray = np.asarray(pcdArray)
        CLI.showInfoMessage('The 3D representation of the image has been done!')


        outputFolder = CONST.OUTPUT_FOLDER + CONST.OUTPUT_PCD + fileName
        pcdFileHandler.pcdFileGenerator(pcdNumpyArray, outputFolder)
        CLI.changeExtension(outputFolder, 'pcd')
        CLI.showInfoMessage('The 3D file has been stored in: ' + outputFolder)

        return True

    except:
        return False
