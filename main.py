from re import A
import discord
from discord.ext import commands
import random
import os
import requests
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents, owner_ids=[906351533426356226])
twitchid = os.getenv('TWITCH_ID')
twitchscrit = os.getenv('TWITCH_SCRIT')
discordtoken = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'{bot.user.name} Login successful!')
    print(f'{str(len(bot.guilds))} Guilds Use.')
    twitchoauth = requests.post(f'https://api.twitch.tv/oauth/token?client_id={twitchid}&client_secret={twitchscrit}&grant_type=client_credentials')
    access_token = json.loads(twitchoauth.text)["access_token"]
    token_type = 'Bearer '
    authorization = token_type + access_token
    print(authorization)

def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


bot.run(discordtoken)