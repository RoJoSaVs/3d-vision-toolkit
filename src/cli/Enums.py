from enum import Enum


# @brief Class to define the file extension key
class FILE_TYPE(Enum):
    IMAGE_FILE = 0
    VIDEO_FILE = 1
    ANY_FILE = 2

# @brief Dictionary with a key value assigned to a file extension used by the system
FILE_EXTENSION_MAP = {
                        FILE_TYPE.IMAGE_FILE: ['.png', '.jpg', '.jpeg'],
                        FILE_TYPE.VIDEO_FILE: ['.mp4', '.avi'],
                        FILE_TYPE.ANY_FILE: ['.*']
                    }
