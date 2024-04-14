# ==========================================================================================
# This is the main file where all the modules are going to be implemented and used, for any
# example of how to use an independent module is show on the mainSample.py file in each 
# folder
# ==========================================================================================

# Importing python modules needed
import sys
import os


# Add 'src/cli' directory to sys.path to use import inside different files
sys.path.append('src/cli/')


# Import of all the external modules
import cli.commandLineInterface as CLI
import cli.Enums as ENUM
from processImage import *
from processVideo import *

# import depth_estimation
# import eulerian_video_magnification
# import image_handler
# import image_stacking
# import pcd_estimator
# import pcd_handler


# @brief Starts the program and check that everything is okay with the commands an parameters
def main():
    try:
        # Check if the file name is provided as an argument
        if (len(sys.argv) != 2):
            CLI.showErrorMessage('An argument is required')
            CLI.showHelpMessage()
            return None


        # Get the file name and path from the argument
        filePathSource = sys.argv[1]

        # Get the just the name of the file
        fileName = os.path.basename(filePathSource)

        # Get the file extension from the argument
        fileExtensionEnum = CLI.checkFileExtension(fileName)
        fileExtensionValue = fileExtensionEnum.value


        # If not an image or a video type file return error message an help
        if (fileExtensionValue == ENUM.FILE_TYPE.ANY_FILE.value):
            CLI.showErrorMessage('The {fileName} file is not an image or a video'.format(fileName = fileName.upper()))
            CLI.showHelpMessage()


        # Process the algorithm as an image WITHOUT Euler Magnification
        elif (fileExtensionValue == ENUM.FILE_TYPE.IMAGE_FILE.value):
            imageProcessResult = processImage(fileName, filePathSource)

            # If the process return False means that something went wrong
            if ((isinstance(imageProcessResult, bool)) and (imageProcessResult == False)):
                CLI.showErrorMessage('The image has not been processed correctly')

            else:
                CLI.showSuccessMessage('The image has been processed!')


        # Process the algorithm as an video WITH Euler Magnification
        elif (fileExtensionValue == ENUM.FILE_TYPE.VIDEO_FILE.value):
            videoProcessResult = processVideo()

            # If the process return False means that something went wrong
            if ((isinstance(videoProcessResult, bool)) and (videoProcessResult == False)):
                CLI.showErrorMessage('The video has not been processed correctly')

            else:
                CLI.showSuccessMessage('The video has been processed!')

        # Exit call when program finished as expected
        return None

    except:
        CLI.showErrorMessage('The program did not work as expected, check that everything is correct')
        CLI.showHelpMessage()




if __name__ == '__main__':
    main()
