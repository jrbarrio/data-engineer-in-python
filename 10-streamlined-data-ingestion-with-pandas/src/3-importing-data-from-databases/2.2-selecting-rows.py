from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

filename = './09-streamlined-data-ingestion-with-pandas/files/data.db'

# Create database engine for data.db
engine = create_engine('sqlite:///' + filename)

# Create query to get hpd311calls records about safety
query = """
SELECT *
FROM hpd311calls
WHERE complaint_type = 'SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()