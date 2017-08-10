import tweepy
import json
from tweepy import OAuthHandler
import pprint

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweets = []
number_of_scraped = 0

with open("finance_handles.txt", 'r') as out:
    for x in out.readlines():
        try:
            # api.get_user(x)
            if number_of_scraped >= 2:
                break
            stuff = api.user_timeline(screen_name = x, since_id = 1234, count = 100, include_rts = True)
            # stuff = api.user_timeline(screen_name = 'TheEconomist', count = 10, include_rts = True)
            tweets.append(stuff)
            number_of_scraped += 1
        except Exception:
            print ('causing error -> ' + x)
        # print (x)

for x in tweets:
    print ("this is for ->" + str(x[0].user.name))
    for y in x:
        print (y.favorite_count)




        # out.write(str(x) + '\n')



# for status in stuff:
#     print (status.text)
