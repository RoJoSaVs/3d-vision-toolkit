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
