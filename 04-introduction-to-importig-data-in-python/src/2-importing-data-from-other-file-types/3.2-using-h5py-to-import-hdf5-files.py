# Import packages
import numpy as np
import h5py

# Assign filename: file
file = './04-introduction-to-importig-data-in-python/files/L-L1_LOSC_4_V1-1126259446-32.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)