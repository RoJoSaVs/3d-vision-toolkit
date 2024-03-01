import imageHandler
import numpy as np
import matplotlib.pyplot as plt


PATH = 'image-source/depth-estimation-dog.png'

# Original image set as a Matrix
numpyArray = imageHandler.imageToArray(PATH)
valueMatrix = imageHandler.imageArrayIterator(numpyArray)

# Matrix to set the depth of each pixel
indexesMatrix = imageHandler.highestToIndex(valueMatrix)

pcdArray = []
for rowIndex in range(0, len(indexesMatrix)):
    for columnIndex in range(0, len(indexesMatrix[rowIndex])):
        pcdArray.append([rowIndex + 1, columnIndex + 1, indexesMatrix[rowIndex][columnIndex]])
