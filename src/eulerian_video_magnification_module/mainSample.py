import videoMotionAmplifier as vma

# Source file
inputVideoFile = 'video/face.mp4'

# Output file folder
outputVideoFile = 'videos-motion'

# Generates the new video with default amplification parameter
vma.videoMotionMagnification(inputVideoFile, outputVideoFile)
