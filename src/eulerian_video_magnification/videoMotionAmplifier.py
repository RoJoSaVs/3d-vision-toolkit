import os


# ==========================================================================================
# Code for the eulerian video magnification taken from https://github.com/vgoehler/PyEVM
# ==========================================================================================
# PyEVM has been imported locally, but if needed it can be installed with pip using:
# 'pip install https://github.com/vgoehler/PyEVM/archive/master.zip'
# ==========================================================================================


# @brief Create the eulerian video magnification to a specific video file
# @param inputVideoFile: Name of the video file that will be magnified
# @param outputVideoFile: Name of the file with the magnification
# @param amplification: Amplification parameter the bigger the number the more moves gonna display
# @note: If amplification parameter is really high can cause some noise on the result
def videoMotionMagnification(inputVideoFile, outputVideoFile, amplification = 2):
    try:
        magnificationStringCommand = f'python -mpython_eulerian_video_magnification {inputVideoFile} -m=MOTION -o={outputVideoFile} -a={amplification}'
        os.system(magnificationStringCommand)
    except NameError:
        raise NameError
