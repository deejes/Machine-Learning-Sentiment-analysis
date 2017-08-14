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
db = client.twitter
collection_name = 'tesla'
collection = db.collection_name

# pdb.set_trace()
# print (collection.count())
#
# print (collection.find()[1000]['text'])
# print (collection.find()[2000]['text'])
# print (collection.find()[4000]['text'])
# print (collection.find()[4000]['text'])
# print (collection.find()[5000]['text'])
# print (collection.find()[6000]['text'])
# print (collection.find()[7000]['text'])
# print (collection.find()[7000]['text'])


for x in range(collection.count()-1):
    if 'Trump' in collection.find()[x]['text']:
        print (x)
#
# pdb.set_trace()
#
# print ('done')
