def load(clean_data, con_engine):
	# Store the data in the schools database
    clean_data.to_sql(
    	name="scores_by_city",
		con=con_engine,
		if_exists="replace",  # Make sure to replace existing data
		index=True,
		index_label="school_id"
    )

def load(clean_data, con_engine):
  clean_data.to_sql(name="scores_by_city", con=con_engine, if_exists="replace", index=True, index_label="school_id")
    
# Call the load function, passing in the cleaned DataFrame
load(cleaned_testing_scores, db_engine)

# Call query the data in the scores_by_city table, check the head of the DataFrame
to_validate = pd.read_sql("SELECT * FROM scores_by_city", con=db_engine)
print(to_validate.head())