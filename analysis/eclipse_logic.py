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
collection = client.twitter_db.eclipse
all_tweets = collection.find()

coord = 0
no_coord = 0
location = 0

# data = []
# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)
# import pdb; pdb.set_trace()

for x in range(collection.count()):
    current_tweet = all_tweets[x]
    # if current_tweet['user']['location']:
    #     print (current_tweet['user']['location'])
    #     # print (current_tweet['geo'])
    #     location += 1
    #     import pdb; pdb.set_trace()
        #
        # if current_tweet['coordinates']:
        # print (current_tweet['coordinates'])
        # coord +=1
        # import pdb; pdb.set_trace()

    # if current_tweet['place']:
    #     print (current_tweet['place']['bounding_box']['coordinates'])
    #     coord += 1
    #     import pdb; pdb.set_trace()
    #
    # else:
    #     no_coord += 1
    if current_tweet["lang"]:
        print (1)

#
# print ('coord',coord, 'no_coord', no_coord, 'location', location)
