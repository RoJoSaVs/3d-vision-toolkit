import videoMotionAmplifier as vma

# Source file
inputVideoFile = '/input/video/face.mp4'

# Output file folder
outputVideoFile = 'output/videos-motion'

# Generates the new video with default amplification parameter
vma.videoMotionMagnification(inputVideoFile, outputVideoFile)
