from pymongo import MongoClient
import pdb
import json
import pprint
from sentiment_analyzer_google_cloudapi import language_analysis

client = MongoClient()
collection = client.twitter_db.wtf


# pprint.pprint (collection.find()[0])

google_scores = []
google_magnitudes = []

# pdb.set_trace()

# for x in range (collection.count()):
for x in range (700,collection.count()):
    # import pdb; pdb.set_trace()
    try:
        current_tweet = collection.find()[x]
        sentiment_object = language_analysis(current_tweet['text'])
        # collection.update_one({'id_str':current_tweet['id_str']},{'$set':{'sentiment.magnitude': sentiment_object.magnitude}})
        # collection.update_one(
        # {'id_str':current_tweet['id_str']},
        # {'$set':{
        # 'sentiment.score': sentiment_object.score
        # }})
        google_scores.append(sentiment_object.score)
        google_magnitudes.append(sentiment_object.magnitude)
    except:
        print('failed')



with open("google_mags5.txt", 'w') as outfile:
    json.dump(google_magnitudes, outfile)
with open("google_scores5.txt", 'w') as outfile:
    json.dump(google_scores, outfile)
