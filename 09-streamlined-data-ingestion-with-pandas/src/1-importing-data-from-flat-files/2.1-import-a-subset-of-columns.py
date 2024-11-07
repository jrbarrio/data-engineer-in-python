# Import pandas as pd
import pandas as pd

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create dataframe from csv using only selected columns
# Read the CSV and assign it to the variable data
data = pd.read_csv("./09-streamlined-data-ingestion-with-pandas/files/vt_tax_data_2016.csv", usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())