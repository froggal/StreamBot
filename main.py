import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents, owner_ids=[906351533426356226])
twitchid = os.getenv('TWITCH_ID')
twitchscrit = os.getenv('TWITCH_SCRIT')
discordtoken = os.getenv('DISCORD_TOKEN')

@bot.event()
async def on_ready():
    print(f'{bot.user.name} Login successful!')
    print(f'{str(len(bot.guilds))} Guilds Use.')

def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)
