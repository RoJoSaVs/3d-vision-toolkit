import unittest
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

sys.path.append('src/')

from pcd_handler.pcdFileHandler import pcdFileGeneratorManual


def check_visual_pcd_file_matplot():
        numpy_array = np.load('./unit-test/testing-folder/bunny.npy')
        coords = numpy_array # Set coords as a numpy array

        # Get x, y, z coords
        x = coords[:, 0]
        y = coords[:, 1]
        z = coords[:, 2]

        # Create the figure and the 3D axis
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Draw the points
        ax.scatter(x, y, z, c='b', marker='o')

        # Set the axis labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Display the figure
        plt.show()

# check_visual_pcd_file_matplot() # Remove comment to get the resulting representation with matplot


class TestPcdFileGeneratorManual(unittest.TestCase):
    def test_pcd_file_generator_manual(self):
        # Loads a sample numpy array
        numpy_array = np.load('./unit-test/testing-folder/bunny.npy')

        # Generate a PCD file
        filename = "./unit-test/testing-folder/test_bunny.pcd"
        pcdFileGeneratorManual(numpy_array, filename)

        # Check if the file is created
        self.assertTrue(os.path.exists(filename))

        # Check if the content of the file is correct
        with open(filename, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 407)  # Ensure the correct number of lines
            self.assertTrue(lines[0].startswith('# .PCD v0.7'))  # Ensure correct header
            self.assertTrue(lines[1].startswith('VERSION 0.7'))  # Ensure correct version
            self.assertTrue(lines[2].startswith('FIELDS x y z rgb'))  # Ensure correct fields
            self.assertTrue(lines[3].startswith('SIZE 4 4 4 4'))  # Ensure correct size
            self.assertTrue(lines[4].startswith('TYPE F F F I'))  # Ensure correct type
            self.assertTrue(lines[5].startswith('COUNT 1 1 1 1'))  # Ensure correct count
            self.assertTrue(lines[6].startswith('WIDTH 397'))  # Ensure correct width
            self.assertTrue(lines[7].startswith('HEIGHT 1'))  # Ensure correct height
            self.assertTrue(lines[8].startswith('POINTS 397'))  # Ensure correct number of points
            self.assertTrue(lines[9].startswith('DATA ascii'))  # Ensure correct data format
            self.assertTrue(lines[10].startswith('-0.065510 0.136240 0.042195 255.000000'))  # Ensure correct first point
            self.assertTrue(lines[406].startswith('-0.071925 0.145450 0.043266 255.000000'))  # Ensure correct last point

        # Clean up
        # os.remove(filename)


if __name__ == '__main__':
    unittest.main()
