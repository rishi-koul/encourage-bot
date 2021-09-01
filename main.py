import discord
import os
my_secret = os.environ['TOKEN']
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer Up",
  "Hang in there",
  "You are a great person/bot"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")

  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print("We have logged in as {0.user}"
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  msg = message.content
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if message.content.startswith("$rishi"):
    await message.channel.send("Rishi you are the best!")

  if message.content.startswith("$HelloImRETARDED"):
    await message.channel.send("HelloImRETARDED you suck")

  if message.content.startswith("$PoSeldOn"):
    await message.channel.send("PoSeldOn you suck")

client.run(my_secret)

  

