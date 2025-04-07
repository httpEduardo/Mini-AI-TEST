import re
import json

def normalize_input(text, slang_dict):
    words = text.lower().split()
    norm = [slang_dict.get(w, w) for w in words]
    return " ".join(norm)

def classify_intent(message, intents):
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in message:
                return intent["tag"]
    return "desconhecido"

def load_slang_dict(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)
