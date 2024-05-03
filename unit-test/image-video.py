import unittest
import cv2
import os
import sys

sys.path.append('src/')


from image_handler.imageVideoConverter import imageToVideo, videoToImage, digitsInFrame

class TestImageVideoFunctions(unittest.TestCase):
    def setUp(self):
        # Create a sample folder with images
        self.images_folder = "./unit-test/testing-folder/test_images"
        os.makedirs(self.images_folder, exist_ok=True)
        # Create a sample image
        self.image = cv2.imread("./input/image-source/street.png")
        cv2.imwrite(os.path.join(self.images_folder, "image1.png"), self.image)
        cv2.imwrite(os.path.join(self.images_folder, "image2.png"), self.image)

        # Create a sample video
        self.video_path = "./unit-test/testing-folder/sample_video.mp4"
        self.output_video_folder = "./unit-test/testing-folder/test_output_video"
        os.makedirs(self.output_video_folder, exist_ok=True)
        self.video = cv2.VideoWriter(self.video_path, 0, 1, (self.image.shape[1], self.image.shape[0]))
        self.video.write(self.image)
        self.video.write(self.image)
        self.video.release()

    def tearDown(self):
        # Clean up created files and folders
        os.remove(self.video_path)
        for file in os.listdir(self.images_folder):
            os.remove(os.path.join(self.images_folder, file))
        os.rmdir(self.images_folder)
        for file in os.listdir(self.output_video_folder):
            os.remove(os.path.join(self.output_video_folder, file))
        os.rmdir(self.output_video_folder)

    def test_image_to_video(self):
        output_video_name = "./unit-test/testing-folder/test_output_video.mp4"
        imageToVideo(self.images_folder, output_video_name, framesPerSecond=1)
        self.assertTrue(os.path.exists(output_video_name))

    def test_video_to_image(self):
        output_images_folder = "./unit-test/testing-folder/test_output_images"
        videoToImage(self.video_path, output_images_folder)
        self.assertTrue(os.path.exists(output_images_folder))
        self.assertEqual(len(os.listdir(output_images_folder)), 2)

    def test_digits_in_frame(self):
        self.assertEqual(digitsInFrame(0), 1)
        self.assertEqual(digitsInFrame(9), 1)
        self.assertEqual(digitsInFrame(10), 2)
        self.assertEqual(digitsInFrame(99), 2)
        self.assertEqual(digitsInFrame(100), 3)

if __name__ == '__main__':
    unittest.main()