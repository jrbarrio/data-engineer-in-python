# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

filename = './04-introduction-to-importig-data-in-python/files/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + filename, echo=True)

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute(text('SELECT Title, Name FROM Album INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID'))
    df = pd.DataFrame(rs.fetchall())
    
    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())