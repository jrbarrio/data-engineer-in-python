import requests
import pandas as pd 

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

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)