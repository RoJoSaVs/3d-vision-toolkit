import unittest
import numpy as np
import sys

sys.path.append('src/')


from image_handler.imageIO import readImage, writeImage, imageToGrayScale

class TestImageFunctions(unittest.TestCase):
    def setUp(self):
        # Create a sample image for testing
        self.image = np.zeros((100, 100, 3), dtype=np.uint8)  # 100x100 black image

    def test_read_write_image(self):
        # Test reading and writing image
        file_path = "./unit-test/testing-folder/test_image.jpg"
        writeImage(file_path, self.image)
        loaded_image = readImage(file_path)

        self.assertTrue(np.array_equal(self.image, loaded_image))

    def test_image_to_grayscale(self):
        # Test converting image to grayscale
        gray_image = imageToGrayScale(self.image)
        expected_shape = (100, 100)  # Grayscale image should have 2 dimensions
        self.assertEqual(gray_image.shape, expected_shape)
        self.assertEqual(len(gray_image.shape), 2)  # Ensure it's grayscale (2 dimensions)


if __name__ == '__main__':
    unittest.main()
