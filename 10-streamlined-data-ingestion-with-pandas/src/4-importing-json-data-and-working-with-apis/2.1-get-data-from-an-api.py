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

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                        headers=headers, 
                        params=params)

# Extract JSON data from the response
data = response.json()
print(data)

# Load data to a dataframe
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)