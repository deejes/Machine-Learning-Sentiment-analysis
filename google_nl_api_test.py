from google.cloud import language

client = language.Client()
document = client.document_from_text('a')
sent_analysis = document.analyze_sentiment()
print (dir(sent_analysis))

'''
def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    dir(sent_analysis)
    sentiment = sent_analysis.sentiment

    ent_analysis = document.analyze_entities()
    dir(ent_analysis)
    entities = ent_analysis.entities

    return sentiment, entities


example_text = 'Python is such a great programming language'
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)
for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience)
'''

#
# def implicit():
#     from google.cloud import storage
#
#     # If you don't specify credentials when constructing the client, the
#     # client library will look for credentials in the environment.
#     storage_client = storage.Client()
#
#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)
