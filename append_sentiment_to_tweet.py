from pymongo import MongoClient
import pdb
import json
import pprint
from sentiment_analyzer_google_cloudapi import language_analysis

client = MongoClient()
collection = client.twitter_db.cloud_api_test


# pprint.pprint (collection.find()[0])

# pdb.set_trace()

for x in range (collection.count()):
    current_tweet = collection.find()[x]
    sentiment_object = language_analysis(current_tweet['text'])
    collection.update_one({'id_str':current_tweet['id_str']},{'$set':{'sentiment.magnitude': sentiment_object.magnitude}})
    collection.update_one(
    {'id_str':current_tweet['id_str']},
    {'$set':{
    'sentiment.score': sentiment_object.score
    }})
