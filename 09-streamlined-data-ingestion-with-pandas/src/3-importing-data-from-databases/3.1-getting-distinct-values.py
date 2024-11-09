from sqlalchemy import create_engine
import pandas as pd

filename = './09-streamlined-data-ingestion-with-pandas/files/data.db'

# Create database engine for data.db
engine = create_engine('sqlite:///' + filename)


# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  FROM hpd311calls;
"""

# Load results of query to a dataframe
issues_and_boros = pd.read_sql(query, engine)

# Check assumption about issues and boroughs
print(issues_and_boros)