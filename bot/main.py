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
    if (message.content.startswith("&gam")):
        await channel.send("kyle says hi goguma")
    elif (message.content.startswith("&goguma")):
        await channel.send("christine says hi gam")
    elif (message.content.startswith("&quiz")):
        await quiz.start(channel)
    elif (message.content.startswith("&stop")):
        await  quiz.start(channel)
    elif (quiz != None and quiz.started):
        await quiz.answer_question(message)



client.run(token)
'''
bot = commands.Bot(command_prefix='!')
quiz = q.Quiz(bot)
token = os.getenv('DISCORD_BOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@bot.command(name = "gam")
async def gam(ctx):
    await ctx.send("kyle says hi goguma")

@bot.command(name = "goguma")
async def gam(ctx):
    await ctx.send("christine says hi gam")

@bot.command(name = "quiz")
async def start(ctx):
    await quiz.start()

@bot.event
async def wait(ctx):
    if (quiz != None and quiz.started):
        await quiz.answer_question(ctx)

bot.run(token)
'''