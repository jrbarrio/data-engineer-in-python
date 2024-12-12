raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)

# Validate the number of columns in the DataFrame
assert len(clean_tax_data.columns) == 5

# Determine if the clean_tax_data DataFrames take type pd.DataFrame
isinstance(clean_tax_data, pd.DataFrame)

# Assert that clean_tax_data is an instance of a pd.DataFrame
assert isinstance(clean_tax_data, pd.DataFrame)

# Assert that clean_tax_data takes is an instance of a string
try:
	assert isinstance(clean_tax_data, str)
except Exception as e:
	print(e)