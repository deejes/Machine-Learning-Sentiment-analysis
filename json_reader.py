import json

with open('love_yourself.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    # print(json.dumps(tweet, indent=4)) # pretty-print
    print (tweet['text'])
    # print (tweet['entities']['hashtags'][0]['text'])
