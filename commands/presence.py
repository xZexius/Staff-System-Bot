import discord
from discord.ext import commands

async def setup(bot):
    @bot.command(name="presence")
    async def presence(ctx, *, presence):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=presence))