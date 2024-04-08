import cv2
import os


# brief Create a video using images folder
# @param imagesFolder: Folder where the images are saved
# @param outputVideoName: Name and path of the resulting video
# @param framesPerSecond: Images that should be displayed in one second (30 frames by default)
# @param imageExtension: The extension of the images used to create the video (png by default)
def imageToVideo(imagesFolder = '', outputVideoName = '', framesPerSecond = 30, imageExtension = '.png'):
    try:
        images = [img for img in os.listdir(imagesFolder) if img.endswith(imageExtension)]
        frame = cv2.imread(os.path.join(imagesFolder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(outputVideoName, 0, framesPerSecond, (width, height))
        cv2.VideoWriter()

        for image in images:
            video.write(cv2.imread(os.path.join(imagesFolder, image)))

        cv2.destroyAllWindows()
        video.release()
    except NameError:
        raise NameError


# brief Create a folder full of video frames as images
# @param videoPath: Video source file
# @param outputVideoPath: Folder where the images are gonna be stored
def videoToImage(videoPath = '', outputVideoPath = ''):
    video = cv2.VideoCapture(videoPath) # Open the video file
    os.makedirs(outputVideoPath, exist_ok=True) # Create the output folder path
    framesInVideo = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    digits = digitsInFrame(framesInVideo)

    # Iterate over frames in the video
    for frameIndex in range(0, framesInVideo):
    # while True:
        ret, frame = video.read() # Read the next frame from the video

        # Break the loop if no more frames are available
        if not ret:
            break

        # Save the depth map to a file in the output folder
        depthMapFilename = os.path.join(outputVideoPath, f'videoFrame_{str(frameIndex).zfill(digits)}.png')
        cv2.imwrite(depthMapFilename, frame)

    # Release the video capture and close the windows
    video.release()
    cv2.destroyAllWindows()


# brief Count the digits that a number has
# @param framesInVideo: Total frames in one video
# @return counter: Digits in of framesInVideo
def digitsInFrame(framesInVideo = 0):
    try:
        digits = 1
        counter = 1
        while ((digits * 10) <= framesInVideo):
            digits = digits * 10
            counter = counter + 1
        return counter

    except NameError:
        raise NameError
