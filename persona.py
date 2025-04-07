def generate_response(intent, message, intents, greentexts):
    if intent == "desconhecido":
        return random.choice([
            "n sei oq cê quis dizer, posta dnv pls",
            "isso parece bait",
            ">no entendy"
        ])

    if intent == "greentext":
        return random.choice(greentexts.get("fail", []))

    for intent_data in intents["intents"]:
        if intent_data["tag"] == intent:
            return random.choice(intent_data["responses"])

    return "???"
