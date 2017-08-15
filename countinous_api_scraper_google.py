import tweepy
import json
from pymongo import MongoClient
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from bson.json_util import dumps
import pdb

# connects to the mongo server, defines a database twitter, and then a collection (table)
client = MongoClient()
collection = client.twitter_db.google

# these lines are setting api keys from api_keys.txt.
with open ("api_keys.txt", "r") as myfile:
    data=myfile.readlines()
consumer_key , consumer_secret , access_token , access_secret = data[0].strip(),data[1].strip(),data[2].strip(),data[3].strip()

# sets up an instance of the api cursor on which calls can be made
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
# pdb.set_trace()

if collection.count() == 0:
    max_id = 896188912883777537
    # current id at 6:58pm on Friday 11th August 2017
else:
    max_id = collection.find()[collection.count()-1]['id']

# pdb.set_trace()


while True:
    results = api.search('#google', count=100, max_id = max_id)
    for result in results:
            if result.lang == 'en' and result.user.followers_count > 100:
                collection.insert_one(result._json)
                print (result._json['text'])
                print (collection.count())
    max_id = collection.find()[collection.count()-1]['id']
