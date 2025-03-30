# Import pandas as pd
import pandas as pd
import random

# Assign the filename: file
file = './06-cleaning-data-in-python/files/ride_sharing_new.csv'

# Read the first 5 rows of the file into a DataFrame: data
ride_sharing = pd.read_csv(file)

ride_sharing['ride_id'] = 0
ride_sharing['ride_id'] = ride_sharing['ride_id'].apply(lambda x: random.randint(1, 1000000)) 

# Find duplicates
duplicates = ride_sharing.duplicated(subset=['ride_id'], keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])