# Import pandas as pd
import pandas as pd
import datetime as dt

# Assign the filename: file
file = './06-cleaning-data-in-python/files/ride_sharing_new.csv'

# Read the first 5 rows of the file into a DataFrame: data
ride_sharing = pd.read_csv(file)

# Save today's date
today = dt.date.today()

ride_sharing['ride_date'] = today + dt.timedelta(days=10)

# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())