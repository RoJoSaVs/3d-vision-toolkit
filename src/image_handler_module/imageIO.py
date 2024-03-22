import cv2


# @brief Read an image from file using opencv and return it as a numpy array.
# @param file_path: The path to the image file
# @return image: The image as a NumPy array
def readImage(file_path):
    try:
        image = cv2.imread(file_path)
        return image
    except NameError:
        raise NameError


# @brief Write an image to file using opencv
# @param file_path: The path to save the image
# @param image: The image as a numpy array
def writeImage(file_path, image):
    try:
        cv2.imwrite(file_path, image)
    except NameError:
        raise NameError


# @brief Transform the color of an matrix image representation to a grayscale representation
# @param matrixImage: Numpy matrix with the pixel colors of the image with the depth estimation
# @return grayImage: Numpy matrix with the value of each pixel of the image in the grayscale
def imageToGrayScale(matrixImage):
    try:
        grayScaleImage = cv2.cvtColor(matrixImage, cv2.COLOR_RGB2GRAY)
        return grayScaleImage
    except NameError:
        raise NameError
