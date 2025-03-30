import sqlalchemy

# Create a connection to the sales database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/sales")

# Query the sales table
raw_sales_data = pd.read_sql("SELECT * FROM sales", db_engine)
print(raw_sales_data)
