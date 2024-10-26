import tweepy, json
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Store credentials in relevant variables
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

# DEPRECATED
# Create your Stream object with credentials
stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)

# Filter your Stream variable
stream.filter(["clinton", "trump", "sanders", "cruz"])