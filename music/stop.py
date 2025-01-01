import discord
from discord.ext import commands
import yt_dlp
import ffmpeg
import os

async def setup(bot):
    @bot.command()
    async def stop(ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        
        if voice_channel:
            if ctx.voice_client:
                ctx.voice_client.stop()
                await ctx.voice_client.disconnect()
                os.remove("song.mp3")
                
                await ctx.send("Music stopped.")
            else:
                await ctx.send("Not in any voice channel.")
        else:
            await ctx.send("First, join a voice channel.")