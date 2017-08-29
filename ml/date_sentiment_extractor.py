import tweepy
import json
from pymongo import MongoClient
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from bson.json_util import dumps
import pdb
import sentiment_mod as s

client = MongoClient()
collection = client.twitter_db.tesla728
all_tweets = collection.find()
result = []
# dates = []


for x in range(collection.count()):
    current_tweet = all_tweets[x]
    sentiment_value, confidence = s.sentiment(current_tweet['text'])
    # print (sentiment_value, ((confidence-0.5)*2))
    sentiment = 0

    if sentiment_value == "pos":
        sentiment = 1
    else:
        sentiment = -1
    result.append(sentiment*confidence)
    # n += 1
    # dates.append(current_tweet['created_at'])
    # if n == 250:
    #     break

# import pdb; pdb.set_trace()

with open("tesla728-us.txt", 'w') as outfile:
    json.dump(result, outfile)
# with open("monsanto_sent_dates.txt", 'w') as outfile:
#     json.dump(dates, outfile)



#
# output = open("sent_test.txt","a")
# output.write(result)
# output.close()
# import pdb; pdb.set_trace()
