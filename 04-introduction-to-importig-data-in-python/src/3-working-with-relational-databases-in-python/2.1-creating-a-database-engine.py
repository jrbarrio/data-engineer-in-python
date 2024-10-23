# Import necessary module
from sqlalchemy import create_engine, inspect

filename = './04-introduction-to-importig-data-in-python/files/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + filename, echo=True)