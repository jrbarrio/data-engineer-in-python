# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = '/home/jorge/Projects/DataCamp/data-engineer-in-python/04-introduction-to-importig-data-in-python/files/titanic_sub.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())