def transform(raw_data):
	# Use .loc[] to only return the needed columns
	raw_data = raw_data.loc[:, ["city", "math_score", "reading_score", "writing_score"]]
	
    # Group the data by city, return the grouped DataFrame
	grouped_data = raw_data.groupby(by=["city"], axis=0).mean()
	return grouped_data

# Transform the data, print the head of the DataFrame
grouped_testing_scores = transform(raw_testing_scores)
print(grouped_testing_scores.head())