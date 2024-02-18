import numpy as np
from PIL import Image


# @brief Function to get the array representation with the pixel values of an image
# @param PATH: Path of the image that will be loaded
# @return numpyArray: Numpy array with the image pixels values
def imageToArray(PATH):
    try:
        image = Image.open(PATH)
        numpyArray = np.array(image, dtype=np.float64)
        return numpyArray
    except NameError:
        raise Exception("Image path not found")


# @brief Function to iterate over each RGBA value in the Numpy Array
# @params imgArray: Matrix with image pixel values RGBA
# @return depthArray: Matrix with the position of each pixel value in a 3D representation
def imageArrayIterator(imgArray):
    try:
        valueMatrix = []
        for row in imgArray:
            newRow = []
            for pixelArray in row:
                rgbValue = pixelArray[0] + pixelArray[1] + pixelArray[2]
                newRow.append(rgbValue)
            valueMatrix.append(newRow)
        return valueMatrix
    except NameError:
        raise Exception("Parameter should be a matrix of pixel values (RGBA)")


# @brief Assign a number based on the descending order of numbers in the matrix given
# @params valueMatrix: Matrix filled with values
# @return matrixIndexed: Matrix with the sorting order of each value in the matrix
def highestToIndex(valueMatrix):
    try:
        maxValue = getHighestValueInMatrix(valueMatrix)
        minValue = getLowestValueInMatrix(valueMatrix, maxValue)
        currentIndex = 1
        while (maxValue > minValue):
            valueMatrix = replaceValuesInMatrix(valueMatrix, maxValue, currentIndex)
            maxValue = getHighestValueInMatrix(valueMatrix)
            currentIndex += 1
        return valueMatrix
    except NameError:
        raise Exception("Error!!")


# @brief Gets the highest value in a matrix
# @param valueMatrix: 2D array with numbers
# @return maxValue: Highest value in the matrix
def getHighestValueInMatrix(valueMatrix):
    try:
        maxValue = 0
        for row in valueMatrix:
            maxInRow = max(row)
            if (maxInRow > maxValue):
                maxValue = maxInRow
        return maxValue
    except NameError:
        raise Exception(NameError)


# @brief Gets the lowest value in a matrix
# @param valueMatrix: 2D array with numbers
# @param maxValue: Starting value to compare with the rest of the matrix
# @return minValue: Lowest value in the matrix
def getLowestValueInMatrix(valueMatrix, maxValue):
    try:
        minValue = maxValue
        for row in valueMatrix:
            minInRow = min(row)
            if (minInRow < minValue):
                minValue = minInRow
        return minValue
    except NameError:
        raise Exception(NameError)


# @brief Replace the values for the ascending index based on descending value
# @params valueMatrix: 2D array with the replaced pixel values
# @params highestValue: Highest value in the matrix
# @params index: Current iteration index
# @return valueMatrix: Matrix with the descending order
def replaceValuesInMatrix(valueMatrix, highestValue, index):
    try:
        for rowIndex in range(0, len(valueMatrix)):
            for columnIndex in range(0, len(valueMatrix[rowIndex])):
                pixel = valueMatrix[rowIndex][columnIndex]
                if (pixel == highestValue):
                    valueMatrix[rowIndex][columnIndex] = index
        return valueMatrix
    except NameError:
        raise Exception(NameError)


# @brief Function to get the highest color value on a pixel
# @params red, green, blue: Color values in decimal representation
# @return Which is the highest color value of the input
def maxRGBColor(red, green, blue):
    try:
        if ((red >= green) and (red >= blue)):
            return 0
        elif ((green >= red) and (green >= blue)):
            return 1
        else:
            return 2
    except NameError:
        raise Exception(NameError)
