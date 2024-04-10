import os
import cv2
import numpy as np


# ==========================================================================
# Code taken from https://github.com/maitek/image_stacking
# ==========================================================================


# @brief Align and stack images with ECC method (slower but more accurate)
# @param fileList: Image list for stacking
# @return stackedImage: Resulting image after stacking
def stackImagesECC(fileList):
    try:
        M = np.eye(3, 3, dtype=np.float32)

        firstImage = None
        stackedImage = None

        for file in fileList:
            image = cv2.imread(file,1).astype(np.float32) / 255
            if firstImage is None:
                # convert to gray scale floating point image
                firstImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                stackedImage = image
            else:
                # Estimate perspective transform
                s, M = cv2.findTransformECC(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY), firstImage, M, cv2.MOTION_HOMOGRAPHY)
                w, h, _ = image.shape
                # Align image to first image
                image = cv2.warpPerspective(image, M, (h, w))
                stackedImage += image

        stackedImage /= len(fileList)
        stackedImage = (stackedImage * 255).astype(np.uint8)
        return stackedImage
    
    except NameError:
        raise NameError


# @brief Method that applies stacking technique to increase the quality of an image
# @param imageFolder: Folder where all the images used for stacking will be stored
# @param resultingImage: Resulting image with the stacking applied
def imageStacking(imageFolder = '', resultingImage = ''):
    try:
        fileList = os.listdir(imageFolder)
        fileList = [os.path.join(imageFolder, x) for x in fileList if x.endswith(('.jpg', '.png','.bmp'))]
        stackedImage = stackImagesECC(fileList)
        cv2.imwrite(resultingImage, stackedImage)
    except NameError:
        raise NameError
