import sys
import os
import numpy as np

# Add 'src/cli' directory to sys.path to use import inside different files
sys.path.append('src/cli/')


import depth_estimation.midasDepthEstimation as midasDepthEstimation
import image_handler.imageIO as imageIO
import image_handler.imageVideoConverter as imageVideoConverter
import eulerian_video_magnification.videoMotionAmplifier as videoMotionAmplifier
import image_stacking.imageStacking as imageStacking
import pcd_estimator.pcdEstimator as pcdEstimator
import pcd_handler.pcdFileHandler as pcdFileHandler
import cli.commandLineInterface as CLI
import cli.constants as CONST


# @brief This method call the functions needed to create the point cloud data file based on an input video
# @param fileName: Name of the file that will be processed
# @param filePathSource: Full folder path where the file exist
# @return If the process has finished returns True otherwise false
def processVideo(fileName, filePathSource):
    try:
        # Name of the folder where the resulting video depth estimation will be stored
        filenameWithoutExtension, _ = os.path.splitext(fileName) # file.ext -> file
        tempFolder = CONST.TEMP_FOLDER + filenameWithoutExtension +'/'

        # Creates the instance and apply the depth estimation for the video
        depthInstance = midasDepthEstimation.DepthEstimation()
        depthInstance.videoDepth(filePathSource, tempFolder)
        CLI.showInfoMessage('Video depth estimation was performed')

        imageToVideoFileInFolder = CONST.TEMP_FOLDER + filenameWithoutExtension + '.avi'
        imageVideoConverter.imageToVideo(tempFolder, imageToVideoFileInFolder)
        CLI.showInfoMessage('Video from images has been created!')

        videoMotionAmplificationFolder = CONST.OUTPUT_FOLDER + CONST.OUTPUT_VIDEO_MOTION_AMPLIFICATION + filenameWithoutExtension
        videoMotionAmplifier.videoMotionMagnification(imageToVideoFileInFolder, videoMotionAmplificationFolder)
        CLI.showInfoMessage('Video motion has been amplified!')

        # Video to images
        amplifiedVideoResultFolder = CLI.getFileInFolder(videoMotionAmplificationFolder)
        amplifiedImagesFromVideoFolder = CONST.TEMP_FOLDER + CONST.TEMP_VIDEO_MOTION_AMPLIFICATION_IMAGES + filenameWithoutExtension
        imageVideoConverter.videoToImage(amplifiedVideoResultFolder, amplifiedImagesFromVideoFolder)
        CLI.showInfoMessage('Video motion divided into frames!')

        # Image stacking
        resultingImageStackingFolder = CONST.OUTPUT_FOLDER + CONST.OUTPUT_STACKING + filenameWithoutExtension + '.png'
        imageStacking.imageStacking(amplifiedImagesFromVideoFolder + '/', resultingImageStackingFolder)
        CLI.showInfoMessage('Video frames stacking process done!')

        # Loads the new image
        resultImageAfterStacking = imageIO.readImage(resultingImageStackingFolder)
        grayScaleImage = imageIO.imageToGrayScale(resultImageAfterStacking)

        # PCD with the stacking result
        pcdArray = pcdEstimator.positionCalculator(resultImageAfterStacking, grayScaleImage)
        pcdNumpyArray = np.asarray(pcdArray)
        CLI.showInfoMessage('The 3D representation of the image has been done!')


        outputFolder = CONST.OUTPUT_FOLDER + CONST.OUTPUT_PCD + fileName
        pcdFileHandler.pcdFileGenerator(pcdNumpyArray, outputFolder)
        CLI.changeExtension(outputFolder, 'pcd')
        CLI.showInfoMessage('The 3D file has been stored in: ' + outputFolder)

        return True

    except:
        return False

