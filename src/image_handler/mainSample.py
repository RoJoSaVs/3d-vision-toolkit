import imageIO
import imageVideoConverter


# ==========================================================================================
# Example of how to use the module for the load and save an image from a numpy matrix
# ==========================================================================================

# Read an image
img_path = "./input/image-source/street.png"
img = imageIO.readImage(img_path)

# Display the shape of the image
print("Image shape:", img.shape)


# Write the image
output_path = "./output/image-source/output.jpg"
imageIO.write_image(output_path, img)


# ==========================================================================================
# Example of how to use the module that convert video to images and vice versa
# ==========================================================================================
# Creates a video from folder images
imageFolder = './temp-files/face_depth'
imageVideoConverter.imageToVideo(imageFolder, './test.avi', 30)

# Generates a folder with images from video frames
videoPath = './output/videos-motion/test_motion_evm_2024-04-07-18-16-19.avi'
outputVideoPath = './temp-files/magnification-depth/'
imageVideoConverter.videoToImage(videoPath, outputVideoPath)
