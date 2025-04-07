import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
nltk.download('punkt')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(sentence, all_words):
    sentence_words = [stem(w) for w in tokenize(sentence)]
    return [1 if w in sentence_words else 0 for w in all_words]
