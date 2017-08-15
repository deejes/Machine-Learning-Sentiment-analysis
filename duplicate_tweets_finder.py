# the function of this script is to take mongo db collection as input
# it should, at present, go through the text of each document, and return false
#  if it has already seen this text.
#  later, we want to incorporate the nl_api, and not do queries for text we've already
# got sentiment for.

import json
from pymongo import MongoClient
from bson.json_util import dumps
import pdb
import mmap


client = MongoClient()
collection = client.twitter_db.tesla

#writes the text of each tweet
with open ("tesla_tweets.txt", "w") as myfile:
    all_records = collection.find()
    for x in range(10):
        myfile.write(all_records[x]['text'])


# https://stackoverflow.com/questions/4940032/search-for-string-in-txt-file-python
# checks if a tweet is in the tesla_tweets.txt file (ie already in the database)
with open('tesla_tweets.txt', 'rb', 0) as file:
    s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    for x in range(20,50):
        if s.find(str.encode(collection.find()[x]['text'])) != -1:
            print('true')
        else:
            print('false')
