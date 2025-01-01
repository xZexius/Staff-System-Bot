import discord
from discord.ext import commands
import json

try:
    with open('config.json', 'r') as file:
        config = json.load(file)
        token = config["token"]
        prefix = config["prefix"]
except FileNotFoundError:
    print("no config.json found")

    
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.load_extension("events.logs")
    await bot.load_extension("commands.rate")
    await bot.load_extension("commands.ban")
    await bot.load_extension("commands.kick")
    await bot.load_extension("commands.warn")
    await bot.load_extension("music.music")
    await bot.load_extension("music.stop")
    await bot.load_extension("commands.presence")
    print("Bot is ready")   

bot.run(token)