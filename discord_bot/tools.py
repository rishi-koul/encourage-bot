import requests
import json
import random
import os


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    return json_data[0]['q'] + " -" + json_data[0]['a']

def get_random_starter_encouragement():
    starter_encouragements = [
        "Cheer Up",
        "Hang in there",
        "You are a great person/bot"
    ]
    return random.choice(starter_encouragements)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

my_secret = os.environ['TOKEN']