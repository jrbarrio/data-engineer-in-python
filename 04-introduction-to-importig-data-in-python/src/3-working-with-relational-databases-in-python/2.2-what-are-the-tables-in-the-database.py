# Import necessary module
from sqlalchemy import create_engine, inspect

filename = './04-introduction-to-importig-data-in-python/files/Chinook.sqlite'

# Create engine: engine
engine = create_engine('sqlite:///' + filename, echo=True)

# Save the table names to a list: table_names
# table_names = engine.table_names() --> DEPRECATED
inspection = inspect(engine)
table_names = inspection.get_table_names()

# Print the table names to the shell
print(table_names)