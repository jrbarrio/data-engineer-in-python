# Import pandas as pd
import pandas as pd

# Read the CSV and assign it to the variable data
data = pd.read_csv("./09-streamlined-data-ingestion-with-pandas/files/vt_tax_data_2016.csv")

# View the first few lines of data
print(data.head())