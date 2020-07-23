import discord
from discord.ext import commands
from discord.utils import get
from random import randint
import os
import random


class TextFunctions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, user):
        "Rolls a random number between 1-100"
        roll = randint(1, 100)
        await ctx.send(roll)

    # Delete text channel messages, 5 is default if no amount is given.
    @commands.command(pass_context=True)
    @commands.has_role("VIRGINS")
    async def clear(self, ctx, amount=5):
        "Clears a specified amount of messages. Default = 5"
        await ctx.channel.purge(limit=amount + 1)


def setup(bot):
    bot.add_cog(TextFunctions(bot))
