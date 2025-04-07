import json
import random
import nltk
import numpy as np
import pickle
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

stemmer = PorterStemmer()
nltk.download('punkt')

with open('data/intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ',']
all_words = [stemmer.stem(w.lower()) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = []
    words = [stemmer.stem(w.lower()) for w in pattern_sentence if w not in ignore_words]
    for w in all_words:
        bag.append(1 if w in words else 0)
    X_train.append(bag)
    y_train.append(tags.index(tag))

model = MultinomialNB()
model.fit(X_train, y_train)

with open('model/model.pkl', 'wb') as f:
    pickle.dump((model, all_words, tags), f)

print("Modelo treinado com sucesso!")
