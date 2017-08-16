import tweepy
import json
from pymongo import MongoClient
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from bson.json_util import dumps
import pprint
import pdb


client = MongoClient()
collection = client.twitter_db.monsanto
test_collection= client.twitter_db.test_collection

#  this is to eiliminate duplicate api calls
#  and to eiliminate multiple tweets from the same person
# with the same text

# Meta Code for what we want to accomplish -
'''
for x in collection.find():
    if x['text'] in new_database:
        matching_tweet = [the record that x[text] was in]
        if x['user'] in matching_tweet:
            orig_db.delete(x)
        else
            x.append(text_sentiment)
            matching_tweet.append(x['user'])
    else:
        api_call = x.api_call
        new_database.insert_one({x.text,api_call,x.user})
        orig_db.x.append(api_call)
'''


# connects to the mongo server, defines a database twitter, and then a collection (table)
pprint.pprint(collection.find()[0])
'''
text = collection.find()[5]['text']
pprint.pprint(collection.find_one({"text": text}))
'''
'''
pprint.pprint(collection.find_one({"user.following": False}))
pprint.pprint(collection.find_one({"user.following": False})['id'])

'''

# pprint.pprint(collection.find_one({"user.following": False}))
'''
text = 'this is my text'
sent = {'a':'a',"b":'b'}
user = [1,2,3,4]

test_collection.insert_one({
                            'text':text,
                            'sentiment' : sent,
                            'users' : user
                            })

pprint.pprint(test_collection.find()[1])
# '''
#
# test_collection.update_one(
#     {'sentiment':'sent'},
#     {"$set": {
#     'follwing': "True"
#     }
#     }
# )
#
# test_collection.update_one(
#     {'sentiment':'sent'},
#     {"$push": {
#     'users': "d"
#     }
#     }
# )


pprint.pprint(test_collection.find()[1])


# these lines are setting api keys from api_keys.txt.
# with open ("api_keys.txt", "r") as myfile:
#     data=myfile.readlines()
# consumer_key , consumer_secret , access_token , access_secret = data[0].strip(),data[1].strip(),data[2].strip(),data[3].strip()
#
# # sets up an instance of the api cursor on which calls can be made
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
# api = tweepy.API(auth)
# # pdb.set_trace()
