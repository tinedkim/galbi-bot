#bot.py
import discord
import os
import quiz as q

client = discord.Client()
quiz = q.Quiz(client)
token = os.getenv('DISCORD_BOT_TOKEN')

client.run(token)

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
