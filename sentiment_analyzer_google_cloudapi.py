#run gcloud_api_key_path.txt after every reboot,
from google.cloud import language
import pdb

# takes text as input, returns a sentiment analysis object from google cloud api.
# call .score and .magnitude on that object to get those two results for the input text.
def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    return document.analyze_sentiment().sentiment


example_text = 'absolute perfection'
sentiment = language_analysis(example_text)
print('score:',sentiment.score,'magnitude:', sentiment.magnitude)
