#bot.py
import discord
import os
import quiz as q

client = discord.Client()
quiz = q.Quiz(client)
token = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    channel = message.channel
    if (message.author == client.user):
        return
    if (message.content.startswith("&command1")):
        await channel.send("sends something back")
    elif (message.content.startswith("&command2")):
        await channel.send("sends something back")
    elif (message.content.startswith("&command3")):
        await quiz.start(channel)
    elif (message.content.startswith("&stop")):
        await quiz.stop(channel)

client.run(token)