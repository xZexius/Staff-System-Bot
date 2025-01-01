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
    print("no config.json found")

def load_warns():
    try:
        with open('database/warns.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_warns(warns):
    with open('database/warns.json', 'w') as file:
        json.dump(warns, file, indent=4)

async def setup(bot):
    @bot.command(name="warn")
    async def warn(ctx, member: discord.Member, *, msg):
        role = discord.utils.get(ctx.guild.roles, id=admin_role_id)
        if role in ctx.author.roles:
            warns = load_warns()
            user_id = str(member.id)

            if user_id not in warns:
                warns[user_id] = {"warns": 0}

            warns[user_id]['warns'] += 1

            save_warns(warns)

            if warns[user_id]['warns'] >= 3:
                await member.ban(reason="+3 Warnings")

            log_channel = bot.get_channel(logs_channel_id)
            mod_channel = bot.get_channel(moderation_channel_id)

            embed = discord.Embed(title="Member Warned", colour=discord.Colour.red())
            embed.add_field(name="Member", value=member.mention, inline=False)
            embed.add_field(name="Reason", value=msg, inline=False)
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=False)
            await log_channel.send(embed=embed)

            embed = discord.Embed(title="Member Warned", colour=discord.Colour.red())
            embed.add_field(name="Member", value=member.mention, inline=False)
            embed.add_field(name="Reason", value=msg, inline=False)
            await mod_channel.send(embed=embed)

        else:
            await ctx.send("You don't have permission to use this command.")