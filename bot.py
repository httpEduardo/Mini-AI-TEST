import random
import json
import pickle
from chatbot.utils import bag_of_words

with open('model/model.pkl', 'rb') as f:
    model, all_words, tags = pickle.load(f)

with open('data/intents.json', 'r') as f:
    intents = json.load(f)

def get_response(msg):
    bow = bag_of_words(msg, all_words)
    result = model.predict([bow])[0]
    tag = tags[result]

    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

    return "Não entendi. Pode repetir?"
