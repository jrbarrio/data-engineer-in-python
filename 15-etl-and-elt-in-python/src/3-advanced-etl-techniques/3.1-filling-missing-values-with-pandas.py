# Fill NaN values with the average from that column
raw_testing_scores["math_score"] = raw_testing_scores["math_score"].fillna(raw_testing_scores["math_score"].mean())

# Print the head of the raw_testing_scores DataFrame
print(raw_testing_scores.head())

def transform(raw_data):
	raw_data.fillna(
    	value={
			# Fill NaN values with column mean
			"math_score": raw_data["math_score"].mean(),
			"reading_score": raw_data["reading_score"].mean(),
			"writing_score": raw_data["writing_score"].mean()
		}, inplace=True
	)
	return raw_data

clean_testing_scores = transform(raw_testing_scores)

# Print the head of the clean_testing_scores DataFrame
print(clean_testing_scores.head())