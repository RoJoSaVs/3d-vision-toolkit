import imageStacking


# Folder where all the images are stored
imagesPath = './temp-files/magnification-depth/'

# File that will be the result of the stacking process
outputPath = './output/stacking-result/image-stacking-result.png'

# Calling the method with the folder with images and the resulting image
imageStacking.imageStacking(imagesPath, outputPath)
