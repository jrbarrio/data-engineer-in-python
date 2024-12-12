# Update the connection string, create the connection object to the schools database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/schools")

# Write the DataFrame to the scores table
cleaned_testing_scores.to_sql(
	name="scores",
	con=db_engine,
	index=False,
	if_exists="replace"
)
