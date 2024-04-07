import numpy as np
import pypcd4 as pcd4


# ==========================================================================================
# The library used for pcd file handling can be found in https://github.com/MapIV/pypcd4
# ==========================================================================================


# @brief Function that helps to converts a numpy array to a pcd file based on the mode
# @param numpyArray: Numpy array that will be stored in a pcd-file
# @param filename: Name of the pcd-file
# @param auto: Select the function to generate the pcd
def pcdFileGenerator(numpyArray, filename, auto = False):
    if(auto):
        pcdFileGeneratorAuto(numpyArray, filename)
    else:
        pcdFileGeneratorManual(numpyArray, filename)


# @brief Function that converts a numpy array to an pcd file
# @param numpyArray: Numpy array that will be stored in a pcd-file
# @param filename: Name of the pcd-file
def pcdFileGeneratorAuto(numpyArray, filename):
    try:
        fields = ('x', 'y', 'z')
        types = (np.float32, np.float32, np.float32)
        pc = pcd4.PointCloud.from_points(numpyArray, fields, types)
        pc.save(filename)

    except NameError:
        raise NameError


# @brief Function that converts a numpy array to an pcd file writing explicit fields
# @param numpyArray: Numpy array that will be stored in a pcd-file
# @param filename: Name of the pcd-file
# @param fields: Fields that will be used in the pcd file ('x', 'y', 'z', 'rgb') by default
# @param types: Numpy types of each field (numpy.float32) by default
def pcdFileGeneratorManual(numpyArray, filename):
    try:
        # Create the file with each field
        with open(filename, 'w') as pcdFile:
            pcdFile.write('# .PCD v0.7 - Point Cloud Data\n')
            pcdFile.write('VERSION 0.7\n')
            pcdFile.write('FIELDS x y z rgb\n')
            pcdFile.write('SIZE 4 4 4 4\n')
            pcdFile.write('TYPE F F F F\n')
            pcdFile.write('COUNT 1 1 1 1\n')
            pcdFile.write('WIDTH {}\n'.format(len(numpyArray)))
            pcdFile.write('HEIGHT 1\n')
            pcdFile.write('POINTS {}\n'.format(len(numpyArray)))
            pcdFile.write('DATA ascii\n')
            for item in numpyArray:
                pcdFile.write('{:.6f} {:.6f} {:.6f} {:d}\n'.format(item[0], item[1], item[2], item[3]))

    except NameError:
        raise NameError


# @brief Function get data from a pcd file and return a Numpy array
# @param filename: Pcd-file that will be loaded
# @return outputArray: Numpy array with the data loaded from the pcd-file
def pcdFileToArray(filename):
    try:
        pc: pcd4.PointCloud = pcd4.PointCloud.from_path(filename)
        outputArray: np.ndarray = pc.numpy()
        return outputArray
    except NameError:
        raise NameError
