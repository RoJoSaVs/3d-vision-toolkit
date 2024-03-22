import matplotlib.pyplot as plt


# ===========================================================================================================================
# The color scale map that should be used is described here https://matplotlib.org/stable/users/explain/colors/colormaps.html
# ===========================================================================================================================


# @brief Get the list of colors on a specific color-map scale
# @param colorScaleName: Color scale name 'Viridis' by default
# @return colorScaleValues: Color scale with its scale as an array
def createColorMapArray(colorScaleName = 'viridis'):
    try:
        # Total numbers in the color-map scale
        numColors = 256
        scaleColors = []

        colorMapScale = plt.get_cmap(colorScaleName)
        for i in range(0, numColors):
            rgbaTuple = colorMapScale(i)
            rgbaList = []

            for rgba in rgbaTuple:
                value = int(rgba * 255)
                rgbaList.append(value)

            scaleColors.append(rgbaList)

        return scaleColors
    except NameError:
        raise NameError


# @brief Gets the index of a pixel value based on the position of a color in the color-map
# @param pixelValue: RGBA value pixel of an image
# @param colorMapArray: List of colors on a specific color-map scale
# @return depthPos: Index in the color-map scale of the pixel color
def pixelToIndex(pixelValue, colorMapArray):
    try:
        depthPos = 0
        lessValue = 765 # 255 * 3
        for index in range(0, len(colorMapArray)):
            red = pixelValue[0] - colorMapArray[index][0]
            green = pixelValue[1] - colorMapArray[index][1]
            blue = pixelValue[2] - colorMapArray[index][2]
            tempValue = abs(red) + abs(green) + abs(blue)
            if (lessValue > tempValue):
                lessValue = tempValue
                depthPos = index
        return depthPos

    except NameError:
        raise NameError
