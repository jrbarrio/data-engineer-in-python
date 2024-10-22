# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('./04-introduction-to-importig-data-in-python/files/ja_data2.mat')

# Print the datatype type of mat
print(type(mat))