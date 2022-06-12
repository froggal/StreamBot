import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents, owner_ids=[906351533426356226])

@bot.event()
async def on_ready():
    print(f'{bot.user.name} Login successful!')
    print(f'{str(len(bot.guilds))} Guilds Use.')