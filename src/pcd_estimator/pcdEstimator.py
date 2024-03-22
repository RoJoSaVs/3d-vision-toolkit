import numpy as np


# @brief Converts an grayscale image array to an array with x, y, z coordinates as array element
# @param matrixImage: Numpy matrix with the pixel colors of the image
# @param grayScaleImage: Image matrix representation in grayscale
# @return positionArray: Array with [x, y, z] coordinates
def positionCalculator(matrixImage, grayScaleImage):
    try:
        if ((len(matrixImage) == len(grayScaleImage)) and (len(matrixImage[0]) == len(grayScaleImage[0]))):
            positionArray = []
            for rowIndex in range(0, len(grayScaleImage)):
                for columnIndex in range(0, len(grayScaleImage[rowIndex])):
                    depth = grayScaleImage[rowIndex][columnIndex]
                    imagePixel = matrixImage[rowIndex][columnIndex]
                    rgb = (imagePixel[0] << 16) | (imagePixel[1] << 8) | imagePixel[2]
                    positionArray.append([columnIndex, rowIndex, depth, rgb])
            return positionArray
        else:
            return []

    except NameError:
        raise NameError


# @brief Map an image represented matrix to an matrix with index of the pixel color in the position
# @param matrixImage: Numpy matrix with the pixel colors of the image with the depth estimation
# @param colorScale: Name of the scale that will be used for the estimation by default it uses viridis
# @return depthIndexMatrix: Matrix filled with the index from 0 to 255 based on the color of the pixel in the position
def imageToWeight(matrixImage, grayScaleImage, colorScale = 'viridis'):
    try:
        positionArray = positionCalculator(grayScaleImage)
        return positionArray

    except NameError:
        raise NameError
