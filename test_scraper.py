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
collection_name = 'tweets'
collection = db.collection_name

# these lines are setting api keys from api_keys.txt.
with open ("api_keys.txt", "r") as myfile:
    data=myfile.readlines()
consumer_key , consumer_secret , access_token , access_secret = data[0].strip(),data[1].strip(),data[2].strip(),data[3].strip()

# sets up an instance of the api cursor on which calls can be made
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

max_id = 896188912883777537
# current id at 6:58pm on Friday 11th August 2017
x = 0

while x < 6:
    results = api.search('earthquake', count=5, max_id = max_id)
    for result in results:
            # print ('')
            # if result.lang == 'en' and result.retweeted and result.favorited and result.user.followers_count > 2000:
            if result.lang == 'en' and result.user.followers_count > 100:
                collection.insert_one(result._json)
                print (result._json['id'])
                print (result._json['text'])
                print (result._json['lang'])

                # print (max_id,collection.count())
                # pdb.set_trace()

    max_id = collection.find()[collection.count()-1]['id'] - 1
    print (max_id,collection.count())
    x += 1
    # for x in range(collection.count()):
    #     print (collection.find()[x]['text'])

    # break

# print (collection.count())
# prints the whole collection as json
# print(dumps(collection.find()))
