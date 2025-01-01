import discord
from discord.ext import commands
import json

try:
    with open('config.json', 'r') as file:
        config = json.load(file)
        admin_role_id = int(config["admin_role_id"])
        logs_channel_id = int(config["logs_channel_id"])
        moderation_channel_id = int(config["moderation_channel_id"])
except FileNotFoundError:
    print("No config.json found")

async def setup(bot):
    @bot.command(name="kick")
    async def kick(ctx, member: discord.Member, *, msg):
        role = discord.utils.get(ctx.guild.roles, id=admin_role_id)
        if role in ctx.author.roles:
            log_channel = bot.get_channel(logs_channel_id)
            mod_channel = bot.get_channel(moderation_channel_id)

            embed = discord.Embed(title="Member Kicked", colour=discord.Colour.red())
            embed.add_field(name="Member", value=member.mention, inline=False)
            embed.add_field(name="Reason", value=msg, inline=False)
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=False)
            await log_channel.send(embed=embed)

            embed = discord.Embed(title="Member Kicked", colour=discord.Colour.red())
            embed.add_field(name="Member", value=member.mention, inline=False)
            embed.add_field(name="Reason", value=msg, inline=False)
            await mod_channel.send(embed=embed)

            await member.kick(reason=msg)

        else:
            await ctx.send("You don't have permission to use this command.")