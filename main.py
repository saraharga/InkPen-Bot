import discord
import os
import random
client = discord.Client()

history = ["https://bit.ly/3NqqwyL","https://bit.ly/3LCfzJd"] 

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
.format(client))

@client.event
async def on_message (message):
  if message.author == client.user:return 

  if message.content.startswith('hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('history'):
   await message.channel.send("Here's our recommendation, check it out here:"+ random.choice(history))

  if message.content.startswith('fiction'):
    await message.channel.send('Here´s our recommendation: "Random Story", check it out here: https://bit.ly/3MwkeNX')

  if message.content.startswith('educational'):
   await message.channel.send('Here´s our recommendation: "Ted Talk", check it out here: https://bit.ly/3x1adC3')


client.run(os.getenv('token'))
