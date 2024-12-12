def transform(raw_data):
	# Use the apply function to extract the street_name from the street_address
    raw_data["street_name"] = raw_data.apply(
   		# Pass the correct function to the apply method
        find_street_name,
        axis=1
    )
    return raw_data

# Transform the raw_testing_scores DataFrame
cleaned_testing_scores = transform(raw_testing_scores)

# Print the head of the cleaned_testing_scores DataFrame
print(cleaned_testing_scores.head())
