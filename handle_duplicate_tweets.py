import tweepy
import json
from pymongo import MongoClient
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from bson.json_util import dumps
import pprint
import pdb

#  this script is to eiliminate duplicate api calls
#  and to eiliminate multiple tweets from the same person
#  with the same text

client = MongoClient()
collection = client.twitter_db.monsanto
test_collection= client.twitter_db.test_collection


# pdb.set_trace()
for x in range(collection.count()-1):
    current_tweet = collection.find()[x]
    matching_tweet = test_collection.find_one({'text':current_tweet['text']})
    # current tweet is not in new database => run api call, create new doc in
    # new_db with text, sentiment, and users array containing current_tweet user
    if matching_tweet == None:
        api_call = current_tweet['text'].upper()
        test_collection.insert_one(
                            {'text': current_tweet['text'],
                            'sentiment': api_call,
                            'users': [current_tweet['user']['id']]}
                            )
    # current tweet is in new database
    else:
        # retweet from same user => delete tweeet from original db
        if current_tweet['user']['id'] in matching_tweet['users']:
            # print ('delete original')
            collection.delete_one({'id':current_tweet['id']})
        # retweet from another user =>
        # 1) get sentiment from new_db and add to current tweet
        # 2) add current_tweet user to matching_tweet users array
        else:
            collection.update_one(
            {'id':current_tweet['id']},
            {'$set':{
            'test_sentiment': matching_tweet['sentiment']
            }})
            test_collection.update_one(
            {'text':current_tweet['text']},
            {'$push':{
            'users' : current_tweet['user']['id']
            }})
