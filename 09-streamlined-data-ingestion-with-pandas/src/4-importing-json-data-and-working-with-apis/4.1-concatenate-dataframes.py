import requests
import pandas as pd 

# Load json_normalize()
from pandas.io.json import json_normalize

import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Store credentials in relevant variables
yelp_api_key = os.getenv('yelp_api_key')

headers = {'Authorization': "Bearer {}".format(yelp_api_key)}

api_url = "https://api.yelp.com/v3/businesses/search"

# Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Concatenate the results, setting ignore_index to renumber rows
cafes = pd.concat([top_50_cafes, next_50_cafes], ignore_index=True)

# Print shape of cafes
print(cafes.shape)