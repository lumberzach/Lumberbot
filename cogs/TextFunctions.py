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
    async def roll(self, ctx):
        roll = randint(1, 100)
        await ctx.send(roll)


def setup(bot):
    bot.add_cog(TextFunctions(bot))
