import imageIO


# ==========================================================================================
# Example of how to use the module for the load and save an image from a numpy matrix
# ==========================================================================================

# Read an image
img_path = "./image-source/street.png"
img = imageIO.readImage(img_path)

# Display the shape of the image
print("Image shape:", img.shape)


# Write the image
output_path = "./image-source/output.jpg"
imageIO.write_image(output_path, img)