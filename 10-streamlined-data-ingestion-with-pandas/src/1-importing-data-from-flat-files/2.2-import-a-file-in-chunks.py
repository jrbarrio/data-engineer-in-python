# Import pandas as pd
import pandas as pd

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("./09-streamlined-data-ingestion-with-pandas/files/vt_tax_data_2016.csv", 
  nrows=500,
  skiprows=500,
  header=None,
  names=vt_data_first500.columns)

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())