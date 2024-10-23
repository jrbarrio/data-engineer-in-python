# Import packages
from sqlalchemy import create_engine,text
import pandas as pd

filename = './04-introduction-to-importig-data-in-python/files/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + filename, echo=True)

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute(text('SELECT * FROM Employee ORDER BY BirthDate'))
    df = pd.DataFrame(rs.fetchall())
    
    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())
