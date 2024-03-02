import numpy as np
import pcdFileHandler as pfh


# ==========================================================================================
# Example of how to use the module for the generation and load of a pcd-file from a 
# numpy matrix
# ==========================================================================================

# Generate some 3D numpy matrix for the example
x = np.linspace(-3, 3, 401)
mesh_x, mesh_y = np.meshgrid(x, x)
z = np.sinc((np.power(mesh_x, 2) + np.power(mesh_y, 2)))
z_norm = (z - z.min()) / (z.max() - z.min())
xyz = np.zeros((np.size(mesh_x), 3))
xyz[:, 0] = np.reshape(mesh_x, -1)
xyz[:, 1] = np.reshape(mesh_y, -1)
xyz[:, 2] = np.reshape(z_norm, -1)

# Example of how to save a numpy array to a pcd-file
pcdOutputPath = './pcd-files/'
filename = 'sample.pcd'
# The output file can be seen on https://imagetostl.com/view-pcd-online
pfh.pcdFileGenerator(xyz, pcdOutputPath + filename)

# Example of how to load a numpy array to a pcd-file
pcdToArray = pfh.pcdFileToArray(pcdOutputPath + filename)