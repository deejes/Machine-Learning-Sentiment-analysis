import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

positive_reivews = open("positive.txt","r").read()
negative_reivews = open("negative.txt","r").read()



all_words = []
documents = [] # will eventually contain tuples with (a review, "pos"/"neg")


# full list - https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
allowed_word_types = ["J"] #only

for p in positive_reivews.split('\n'):
    documents.append((p,"pos"))
    words = word_tokenize(p)
    words_pos = nltk.pos_tag(words)
    for w in words_pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for p in negative_reivews.split('\n'):
    documents.append((p,"neg"))
    words = word_tokenize(p)
    words_pos = nltk.pos_tag(words)
    for w in words_pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

save_documents = open("pickled_algos/documents.pickle", "wb")
pickle.dump(documents, save_documents)
save_documents.close()

#creats a dictionary like structure of key value pairs
# with words as keys and number of occurances as values
all_words = nltk.FreqDist(all_words)
import pdb; pdb.set_trace()

# creates a list of the top <n>% most commonly occuring words in all_words
size_words_features = int(len(all_words)*.4)
word_features = [all_words.most_common()[x][0] for x in range(size_words_features)]

word_features_pickle = open("pickled_algos/word_features5k.pickle","wb")
pickle.dump(word_features,word_features_pickle)
word_features_pickle.close()

# will take a sentence as input, return a list, with (word in all_words, (if that word is sentence))
def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

#  TODO : take a look at featuresets carefully

featuresets = [(find_features(rev), category) for (rev, category) in documents]
# import pdb; pdb.set_trace()
random.shuffle(featuresets)
# print(len(featuresets))


save_featuresets = open("pickled_algos/featuresets.pickle","wb")
pickle.dump(featuresets, save_featuresets)
save_featuresets.close()



testing_set = featuresets[10000:]
training_set = featuresets[:10000]

# Classifiers
########################################################

# C1
classifier = nltk.NaiveBayesClassifier.train(training_set)
print ("original naive bayes algo accuracy %", nltk.classify.accuracy(classifier,testing_set))

save_classifier = open("pickled_algos/originalnaivebayes5k.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

# C2
MNB_classifier = SklearnClassifier(MultinomialNB()).train(training_set)
print ("MultinomialNB_classifier accuracy", nltk.classify.accuracy(MNB_classifier,testing_set))

save_classifier = open("pickled_algos/MNB_classifier5k.pickle","wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

# C3
BernoulliNB_classifier = SklearnClassifier(BernoulliNB()).train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

save_classifier = open("pickled_algos/BernoulliNB_classifier5k.pickle","wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()

# C4
LogisticRegression_classifier = SklearnClassifier(LogisticRegression()).train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

save_classifier = open("pickled_algos/LogisticRegression_classifier5k.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()

# C5
LinearSVC_classifier = SklearnClassifier(LinearSVC()).train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

save_classifier = open("pickled_algos/LinearSVC_classifier5k.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

####################################################################################

voted_classifier = VoteClassifier(classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                  LinearSVC_classifier)

print("voted_classifier accuracy percent:", nltk.classify.accuracy(voted_classifier, testing_set))



def sentiment(text):
    features = find_features(text)
    return voted_classifier.classify(features)
