import discord
from discord_bot import tools

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}"
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("$inspire"):
    quote = tools.get_quote()
    await message.channel.send(quote)

  msg = message.content
  
  if any(word in msg for word in tools.sad_words):
    await message.channel.send(tools.get_random_starter_encouragement())

  if message.content.startswith("$rishi"):
    await message.channel.send("Rishi you are the best!")

  if message.content.startswith("$HelloImRETARDED"):
    await message.channel.send("HelloImRETARDED you suck")

  if message.content.startswith("$PoSeldOn"):
    await message.channel.send("PoSeldOn you suck")



if __name__ == '__main__':
  client.run(tools.my_secret)