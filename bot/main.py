#bot.py
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '&')
token = os.getenv('DISCORD_BOT_TOKEN')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'gam')
async def gam(ctx):
    response = "kyle says hi goguma"
    await ctx.send(response)

@bot.command(name = 'goguma')
async def goguma(ctx):
    response = "christine says hi gam"
    await ctx.send(response)

bot.run(token)