import unittest
import cv2
import os
import torch
import sys

sys.path.append('src/')

from depth_estimation.midasDepthEstimation import DepthEstimation

class TestDepthEstimation(unittest.TestCase):
    def setUp(self):
        self.depth_estimator = DepthEstimation()

    def test_image_depth(self):
        input_image_path = "./input/image-source/street.png"
        output_depth_path = "./unit-test/testing-folder/depth_map.jpg"

        # Test image depth estimation
        depth_map = self.depth_estimator.imageDepth(input_image_path)
        self.assertIsNotNone(depth_map)
        cv2.imwrite(output_depth_path, depth_map)  # Save the depth map for manual inspection


    def test_video_depth(self):
        input_video_path = "./input/video/face.mp4"
        output_depth_folder = "./unit-test/testing-folder/depth_maps/"
        
        # Create a sample video
        video = cv2.VideoWriter(input_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
        for _ in range(10):  # Write 10 frames
            frame = cv2.imread("./unit-test/testing-folder/depth_maps/depthMap_0.png")
            video.write(frame)
        video.release()
        
        # Test video depth estimation
        self.depth_estimator.videoDepth(input_video_path, output_depth_folder)
        depth_map_files = os.listdir(output_depth_folder)
        self.assertEqual(len(depth_map_files), 10)  # Ensure 10 depth maps were generated

        # Clean up created files
        os.remove(input_video_path)
        for file in depth_map_files:
            os.remove(os.path.join(output_depth_folder, file))
        os.rmdir(output_depth_folder)


if __name__ == '__main__':
    unittest.main()
