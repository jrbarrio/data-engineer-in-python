# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = './06-cleaning-data-in-python/files/ride_sharing_new.csv'

# Read the first 5 rows of the file into a DataFrame: data
ride_sharing = pd.read_csv(file)

ride_sharing['tire_sizes'] = 29
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())