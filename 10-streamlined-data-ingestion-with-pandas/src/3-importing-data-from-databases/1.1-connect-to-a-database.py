# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine, inspect

filename = './09-streamlined-data-ingestion-with-pandas/files/data.db'

# Create the database engine
engine = create_engine('sqlite:///' + filename, echo=True)

# Save the table names to a list: table_names
# table_names = engine.table_names() --> DEPRECATED
inspection = inspect(engine)
table_names = inspection.get_table_names()

# Print the table names to the shell
print(table_names)