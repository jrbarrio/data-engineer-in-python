from sqlalchemy import create_engine
import pandas as pd

filename = './09-streamlined-data-ingestion-with-pandas/files/data.db'

# Create database engine for data.db
engine = create_engine('sqlite:///' + filename)

# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32
  OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())