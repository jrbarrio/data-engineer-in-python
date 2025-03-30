# Parse the street_address from the dictionary
street_address = school.get("street_address")

# Parse the scores dictionary
scores = school.get("scores")

# Try to parse the math, reading and writing values from scores
math_score = scores.get("math", 0)
reading_score = scores.get("reading", 0)
writing_score = scores.get("writing", 0)

print(f"Street Address: {street_address}")
print(f"Math: {math_score}, Reading: {reading_score}, Writing: {writing_score}")
