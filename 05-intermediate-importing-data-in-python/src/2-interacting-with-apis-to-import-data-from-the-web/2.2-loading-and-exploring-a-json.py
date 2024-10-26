import json

file = './05-intermediate-importing-data-in-python/files/a_movie.json'

# Load JSON: json_data
with open(file) as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])