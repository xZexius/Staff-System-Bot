import discord
from discord.ext import commands
import os
import yt_dlp as youtube_dl


async def setup(bot):
    @bot.command(name="song")
    async def song(ctx, url):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            em8 = discord.Embed(title = "Music Is Currently Playing", description = 'Please wait for the current playing music to end.\nMusic provided by {ctx.author.mention}',color = ctx.author.color)
            await ctx.send(embed = em8)
            return

        voiceChannel = discord.utils.get(ctx.guild.voice_channels)
        await voiceChannel.connect()
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        em6 = discord.Embed(title = "Downloading Youtube Music", description = f'{url}\n\nPlease wait for bot to setup the music you provide.\nMusic provided by {ctx.author.mention}',color = ctx.author.color)
        await ctx.send(embed = em6, delete_after = 2)
        await ctx.message.delete()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '196',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        em1 = discord.Embed(title = "Now Listening Youtube Music", description = f'{url}\n\nPlease use %leave first to change music.\nMusic provided by {ctx.author.mention}',color = ctx.author.color)

        videoID = url.split("watch?v=")[1].split("&")[0]

        em1.set_thumbnail(url = f'https://img.youtube.com/vi/{videoID}/default.jpg'.format(videoID = videoID))
        await ctx.send(embed = em1)