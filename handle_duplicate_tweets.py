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
#  (for tweets with same text)
#  and to eiliminate multiple tweets from the same person
#  with the same text

client = MongoClient()
collection = client.twitter_db.google_test_db
test_collection= client.twitter_db.google_test_new_db

print(collection.count())
print(test_collection.count())
pdb.set_trace()
# collection_count = collectioncount()-1
for x in range(collection.count()-1):
    current_tweet = collection.find()[x]
    matching_tweet = test_collection.find_one({'text':current_tweet['text']})
    # current tweet is not in new database => run api call, create new doc in
    # new_db with text, sentiment, and users array containing current_tweet user

    # TO DO Append results of api call to original tweet
    if matching_tweet == None:
        api_call = current_tweet['text'].upper()
        test_collection.insert_one(
                            {'text': current_tweet['text'],
                            'sentiment': api_call,
                            'users': [current_tweet['user']['id_str']]}
                            )
    # current tweet is in new database
    else:
        # retweet from same user => delete tweeet from original db
        if current_tweet['user']['id_str'] in matching_tweet['users']:
            # print ('delete original')
            collection.delete_one({'user.id_str':current_tweet['user']['id_str']})
        # retweet from another user =>
        # 1) get sentiment from new_db and add to current tweet
        # 2) add current_tweet user to matching_tweet users array
        else:
            collection.update_one(
            {'id_str':current_tweet['id_str']},
            {'$set':{
            'test_sentiment': matching_tweet['sentiment']
            }})
            print(current_tweet['user']['id_str'])
            test_collection.update_one(
            {'text':current_tweet['text']},
            {'$push':{
            'users' : current_tweet['user']['id_str']
            }})
