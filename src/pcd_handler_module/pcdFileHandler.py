import numpy as np
import pypcd4 as pcd4


# ==========================================================================================
# The library used for pcd file handling can be found in https://github.com/MapIV/pypcd4
# ==========================================================================================


# @brief Function that converts a numpy array to an pcd file
# @param numpyArray: Numpy array that will be stored in a pcd-file
# @param filename: Name of the pcd-file
def pcdFileGenerator(numpyArray, filename):
    try:
        fields = ('x', 'y', 'z')
        types = (np.float32, np.float32, np.float32)
        pc = pcd4.PointCloud.from_points(numpyArray, fields, types)
        pc.save(filename)

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
