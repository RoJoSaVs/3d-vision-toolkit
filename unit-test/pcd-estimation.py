import unittest
import numpy as np
import sys

sys.path.append('src/')

from pcd_estimator.pcdEstimator import positionCalculator

class TestPositionCalculator(unittest.TestCase):
    def test_position_calculator(self):
        # Create a sample grayscale image
        gray_scale_image = np.array([[100, 150, 200],
                                     [50, 100, 150],
                                     [25, 50, 75]])

        # Create a sample RGB image
        rgb_image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                              [[128, 128, 128], [64, 64, 64], [32, 32, 32]],
                              [[0, 0, 0], [255, 255, 255], [128, 128, 128]]])

        expected_positions = [
            [0, 0, 100, 16711680], [1, 0, 150, 65280], [2, 0, 200, 255],
            [0, 1, 50, 8421504], [1, 1, 100, 4210752], [2, 1, 150, 2105376],
            [0, 2, 25, 0], [1, 2, 50, 16777215], [2, 2, 75, 8421504]
        ]

        # Test position calculator
        positions = positionCalculator(rgb_image, gray_scale_image)
        self.assertEqual(len(positions), 9)  # Ensure the correct number of positions are returned
        self.assertEqual(positions, expected_positions)

if __name__ == '__main__':
    unittest.main()
