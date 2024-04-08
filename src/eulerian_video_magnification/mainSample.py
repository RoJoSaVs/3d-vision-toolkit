import videoMotionAmplifier as vma

# Source file
inputVideoFile = './test.avi'
# inputVideoFile = '/input/video/face.mp4'

# Output file folder
# outputVideoFile = 'output/videos-motion'
outputVideoFile = 'output/videos-motion'

amplification = 20

# Generates the new video with default amplification parameter
vma.videoMotionMagnification(inputVideoFile, outputVideoFile, amplification)
