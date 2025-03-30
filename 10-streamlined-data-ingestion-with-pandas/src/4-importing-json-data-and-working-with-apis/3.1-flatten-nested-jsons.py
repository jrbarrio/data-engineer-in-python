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
params = {'term': 'cafe', 'location': 'NYC'}

api_url = "https://api.yelp.com/v3/businesses/search"

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                headers=headers, 
                params=params)

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
             sep='_')

# View data
print(cafes.head())