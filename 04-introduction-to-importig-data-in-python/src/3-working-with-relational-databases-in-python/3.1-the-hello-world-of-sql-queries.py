# Import packages
from sqlalchemy import create_engine,text
import pandas as pd

filename = './04-introduction-to-importig-data-in-python/files/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + filename, echo=True)

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute(text('SELECT * FROM Album'))

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())