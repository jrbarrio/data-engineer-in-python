# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = '/home/jorge/Projects/DataCamp/data-engineer-in-python/04-introduction-to-importig-data-in-python/files/digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.to_numpy()

# Print the datatype of data_array to the shell
print(type(data_array))