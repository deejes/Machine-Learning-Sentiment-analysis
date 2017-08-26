import pdb; pdb.set_trace()
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


with open ("../api_keys.txt", "r") as myfile:
    data=myfile.readlines()
consumer_key , consumer_secret , access_token , access_secret = data[0].strip(),data[1].strip(),data[2].strip(),data[3].strip()

# sets up an instance of the api cursor on which calls can be made
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
# api = tweepy.API(auth)


class listener(StreamListener):
    def on_data(self,data):
        try:
            all_data =json.loads (data)
            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet,sentiment_value,confidence)
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
            return True
        except:
            print ('failed')
            return True

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


twitter_stream = Stream(auth,listener())
twitter_stream.filter(track=["happy"])
