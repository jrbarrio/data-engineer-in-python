# Import numpy
import numpy as np

# Assign the filename: file
file = '/home/jorge/Projects/DataCamp/data-engineer-in-python/04-introduction-to-importig-data-in-python/files/digits_header.csv'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

# Print data
print(data)