import discord
from discord.ext import commands
from discord.ui import View, Select
import json

try:
    with open('config.json', 'r') as file:
        config = json.load(file)
        admin_role_id = int(config["admin_role_id"])
        rate_channel_id = int(config["rate_channel_id"])
except FileNotFoundError:
    print("No config.json found")
    admin_role_id = None
    rate_channel_id = None

class categorySelect(View):
    def __init__(self, staff_to_rate=None):
        super().__init__(timeout=None)
        self.staff_to_rate = staff_to_rate

        self.select = Select(
            placeholder="Rate the Staff",
            options=[
                discord.SelectOption(label="⭐", value="1"),
                discord.SelectOption(label="⭐⭐", value="2"),
                discord.SelectOption(label="⭐⭐⭐", value="3"),
                discord.SelectOption(label="⭐⭐⭐⭐", value="4"),
                discord.SelectOption(label="⭐⭐⭐⭐⭐", value="5"),
            ]
        )
        self.select.callback = self.select_option_callback
        self.add_item(self.select)

    async def select_option_callback(self, interaction: discord.Interaction):
        staff_member = self.staff_to_rate
        rates_channel = interaction.client.get_channel(rate_channel_id)

        if self.select.values[0] in ["1", "2", "3", "4", "5"]:
            embed = discord.Embed(
                description="> Thanks for rating the staff attention, your ticket has been marked as solved.",
                color=discord.Color.green()
            )
            embed2 = discord.Embed(
                title="New Staff Rated",
                colour=discord.Colour.green()
            )
            embed2.add_field(name="Stars", value="⭐" * int(self.select.values[0]), inline=False)
            embed2.add_field(name="Staff", value=staff_member.mention, inline=False)
            if rates_channel:
                await rates_channel.send(embed=embed2)
            await interaction.response.send_message(embed=embed)

async def setup(bot):
    @bot.command(name="rate")
    async def rate(ctx):
        role = discord.utils.get(ctx.guild.roles, id=admin_role_id)
        if role in ctx.author.roles:
            embed = discord.Embed(
                description="> Staff marked this as solved, please select a rating in order to close the ticket.",
                colour=discord.Colour.green()
            )
            category = categorySelect(staff_to_rate=ctx.author)
            await ctx.send(embed=embed, view=category)
        else:
            await ctx.send("You don't have permission to use this command.")
