# Python imports
import os


# Import external modules
import constants as const
import Enums as ENUMS


# @brief Show the help commands related with the code
def showHelpMessage():
    print(const.DividerColor + '----------------------------------------------------------------------------------------------------------------')
    print(const.InfoColor, end = '')
    print('This program receives a file as argument.')
    print('Usage: python program.py file')
    print('Example: python program.py file.txt')
    print(const.DividerColor + '----------------------------------------------------------------------------------------------------------------')
    print(const.DefaultColor)


# @brief Show an error message in console
def showErrorMessage(message):
    print(const.DividerColor + '----------------------------------------------------------------------------------------------------------------')
    print(const.ErrorColor, end = '')
    print(f'Error: {message}')
    print(const.DividerColor + '----------------------------------------------------------------------------------------------------------------')
    print(const.DefaultColor)


# @brief Show success message in console
def showSuccessMessage(message):
    print(const.DividerColor + '----------------------------------------------------------------------------------------------------------------')
    print(const.SuccessColor, end = '')
    print(f'Success: {message}')
    print(const.DividerColor + '----------------------------------------------------------------------------------------------------------------')
    print(const.DefaultColor)


# @brief Show success message in console
def showInfoMessage(message):
    print(const.DividerColor + '----------------------------------------------------------------------------------------------------------------')
    print(const.InfoColor, end = '')
    print(f'Info: {message}')
    print(const.DividerColor + '----------------------------------------------------------------------------------------------------------------')
    print(const.DefaultColor)


# @brief Check that the file is an image or a video
# @param fileName: Name of the file that will be processed
# @return FILE_TYPE: Enum with the file type key value assigned
def checkFileExtension(fileName):
    try:
        _, fileExtension = os.path.splitext(fileName)

        if (fileExtension.lower() in ENUMS.FILE_EXTENSION_MAP[ENUMS.FILE_TYPE.IMAGE_FILE]):
            return ENUMS.FILE_TYPE.IMAGE_FILE
        
        elif(fileExtension.lower() in ENUMS.FILE_EXTENSION_MAP[ENUMS.FILE_TYPE.VIDEO_FILE]):
            return ENUMS.FILE_TYPE.VIDEO_FILE
        
        else:
            return ENUMS.FILE_TYPE.ANY_FILE
    except:
        showErrorMessage('The files cannot be processed')


# @brief Change the extension of a file
# @param filePath: Folder location where the file to be renamed is
# @param newExtension: The new extension of the file
def changeExtension(filePath, newExtension):
    baseName, _ = os.path.splitext(filePath)
    newFilePath = baseName + "." + newExtension
    os.rename(filePath, newFilePath)
