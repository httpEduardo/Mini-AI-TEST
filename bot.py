import json
import random
from utils import normalize_input, classify_intent, load_slang_dict
from persona import generate_response

with open("data/intents.json", encoding='utf-8') as f:
    intents = json.load(f)

with open("data/greentexts.json", encoding='utf-8') as f:
    greentexts = json.load(f)

slang_dict = load_slang_dict("data/slang_dict.json")

def get_response(message):
    norm = normalize_input(message, slang_dict)
    intent = classify_intent(norm, intents)
    return generate_response(intent, message, intents, greentexts)