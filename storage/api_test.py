import tweepy
import json
from pymongo import MongoClient
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from bson.json_util import dumps

# connects to the mongo server, defines a database twitter, and then a collection (table)
client = MongoClient()
db = client.twitter
collection_name = 'tweets'
collection = db.[collection_name]

# these lines are setting api keys from api_keys.txt.
with open ("api_keys.txt", "r") as myfile:
    data=myfile.readlines()
consumer_key , consumer_secret , access_token , access_secret = data[0].strip(),data[1].strip(),data[2].strip(),data[3].strip()

# sets up an instance of the api cursor on which calls can be made
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#  return value of api.search is a list like object, needs to be iterated through
result = api.search('google',count=10,max_id = 892796899684399104)

# dumps dictionary form of each result into the database
for result in result:
    collection.insert_one(result._json)

print (collection.count())

# prints the whole collection as json
print(dumps(collection.find()))
