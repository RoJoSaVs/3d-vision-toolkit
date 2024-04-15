# Defining color to print console messages
C_END      = '\33[0m'
C_BOLD     = '\33[1m'
C_ITALIC   = '\33[3m'
C_URL      = '\33[4m'
C_BLINK    = '\33[5m'
C_BLINK2   = '\33[6m'
C_SELECTED = '\33[7m'

C_BLACK  = '\33[30m'
C_RED    = '\33[31m'
C_GREEN  = '\33[32m'
C_YELLOW = '\33[33m'
C_GRAY   = '\33[34m'
C_BLUE   = '\33[94m'
C_VIOLET = '\33[35m'
C_LIGHT_BLUE  = '\33[36m'
C_WHITE  = '\33[37m'


# Terminal colors and styles
ErrorColor = C_BOLD + C_RED
InfoColor = C_BOLD + C_LIGHT_BLUE
SuccessColor = C_BOLD + C_GREEN
DividerColor = C_BOLD + C_YELLOW
DefaultColor = C_END

# =========================================================================== #
# Folder path to store temporary files
TEMP_FOLDER = './temp-files/'
TEMP_VIDEO_MOTION_AMPLIFICATION_IMAGES = 'videos-motion-images/'

# Folder path to store the resulting files
OUTPUT_FOLDER = './output/'
OUTPUT_PCD = 'pcd-files/'
OUTPUT_STACKING = 'stacking-result/'
OUTPUT_VIDEO_MOTION_AMPLIFICATION = 'videos-motion/'
