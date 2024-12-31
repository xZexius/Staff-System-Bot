import discord
from discord.ext import commands
import json

try:
    with open('config.json', 'r') as file:
        config = json.load(file)
        logs_channel_id = int(config["logs_channel_id"])
except FileNotFoundError:
    print("no config.json found")


async def setup(bot):
    @bot.event
    async def on_message_delete(message):
        if message.author.bot:
            return
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Message Deleted", colour=discord.Colour.red())
        embed.add_field(name="Author", value=message.author.mention, inline=False)
        embed.add_field(name="Channel", value=message.channel.mention, inline=False)
        embed.add_field(name="Message", value=message.content, inline=False)
        await channeltosend.send(embed=embed)
    
    @bot.event
    async def on_message_edit(before, after):
        if before.author.bot:
            return
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Message Edited", colour=discord.Colour.blue())
        embed.add_field(name="Author", value=before.author.mention, inline=False)
        embed.add_field(name="Channel", value=before.channel.mention, inline=False)
        embed.add_field(name="Message", value=before.content, inline=False)
        embed.add_field(name="New Message", value=after.content, inline=False)
        await channeltosend.send(embed=embed)
        
    @bot.event
    async def on_member_join(member):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Member Joined", colour=discord.Colour.green())
        embed.add_field(name="Member", value=member.mention, inline=False)
        await channeltosend.send(embed=embed)
        
    @bot.event
    async def on_member_remove(member):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Member Left", colour=discord.Colour.red())
        embed.add_field(name="Member", value=member.mention, inline=False)
        await channeltosend.send(embed=embed)
    
    @bot.event
    async def on_guild_channel_create(channel):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Channel Created", colour=discord.Colour.green())
        embed.add_field(name="Channel", value=channel.mention, inline=False)
        await channeltosend.send(embed=embed)
        
    @bot.event
    async def on_guild_channel_delete(channel):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Channel Deleted", colour=discord.Colour.red())
        embed.add_field(name="Channel", value=channel.mention, inline=False)
        await channeltosend.send(embed=embed)
    
    @bot.event
    async def on_guild_role_create(role):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Role Created", colour=discord.Colour.green())
        embed.add_field(name="Role", value=role.mention, inline=False)
        await channeltosend.send(embed=embed)
        
    @bot.event
    async def on_guild_role_delete(role):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Role Deleted", colour=discord.Colour.red())
        embed.add_field(name="Role", value=role.mention, inline=False)
        await channeltosend.send(embed=embed)
    
    @bot.event
    async def on_guild_emojis_update(guild):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Emojis Updated", colour=discord.Colour.green())
        embed.add_field(name="Guild", value=guild.mention, inline=False)
        await channeltosend.send(embed=embed)
        
    @bot.event
    async def on_guild_stickers_update(guild):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Stickers Updated", colour=discord.Colour.green())
        embed.add_field(name="Guild", value=guild.mention, inline=False)
        await channeltosend.send(embed=embed)
    
    @bot.event
    async def on_member_ban(member):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Member Banned", colour=discord.Colour.red())
        embed.add_field(name="Member", value=member.mention, inline=False)
        await channeltosend.send(embed=embed)
        
    @bot.event
    async def on_member_unban(member):
        channeltosend = bot.get_channel(logs_channel_id)
        embed = discord.Embed(title="Member Unbanned", colour=discord.Colour.green())
        embed.add_field(name="Member", value=member.mention, inline=False)
        await channeltosend.send(embed=embed)