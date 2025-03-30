# Load libraries
import pandas as pd
from sqlalchemy import create_engine

filename = './09-streamlined-data-ingestion-with-pandas/files/data.db'

# Create the database engine
engine = create_engine('sqlite:///' + filename)

# Load hpd311calls without any SQL
hpd_calls = pd.read_sql("hpd311calls", engine)

# View the first few rows of data
print(hpd_calls.head())

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""

# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())