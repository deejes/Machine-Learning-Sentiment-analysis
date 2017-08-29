from pymongo import MongoClient
import pdb
import json
import pprint
from sentiment_analyzer_google_cloudapi import language_analysis

client = MongoClient()
collection = client.twitter_db.happy


# pprint.pprint (collection.find()[0])

scores = []
magnitudes = []

# pdb.set_trace()

# for x in range (collection.count()):
for x in range (500,collection.count()):
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
        scores.append(sentiment_object.score)
        magnitudes.append(sentiment_object.magnitude)
    except:
        print('failed')



with open("happy_mags2.txt", 'w') as outfile:
    json.dump(magnitudes, outfile)
with open("happy_scores2.txt", 'w') as outfile:
    json.dump(scores, outfile)
