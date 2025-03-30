# Import pandas as pd
import pandas as pd
import random

# Assign the filename: file
file = './06-cleaning-data-in-python/files/ride_sharing_new.csv'

# Read the first 5 rows of the file into a DataFrame: data
ride_sharing = pd.read_csv(file)

# Strip duration of minutes
ride_sharing['duration'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration'] = ride_sharing['duration'].astype('int')

ride_sharing['user_birth_year'] = 1978

ride_sharing['ride_id'] = 0
ride_sharing['ride_id'] = ride_sharing['ride_id'].apply(lambda x: random.randint(1, 1000000)) 

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0