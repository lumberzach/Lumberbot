import discord
from discord.ext import commands
from discord.utils import get
from random import randint
import pyowm
from pyowm.owm import OWM
import dotenv
from dotenv import load_dotenv
import os
import random
import datetime
# from discord.ext import commands, timers
# from covid19_data import JHU


load_dotenv()



owmapi = os.getenv("owm_key")

class TextFunctions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx):
        "Rolls a random number between 1-100"
        roll = randint(1, 100)
        await ctx.send(roll)

    @commands.command()
    async def covid(self, ctx):
        "Reports current Covid19 Case Count in AZ"
        await ctx.send("The amount of confirmed Covid19 cases in AZ is currently " + str(JHU.Arizona.confirmed))



    # Delete text channel messages, 5 is default if no amount is given.
    @commands.command(pass_context=True)
    @commands.has_role("VIRGINS")
    async def clear(self, ctx, amount=5):
        "Clears a specified amount of messages. Default = 5"
        await ctx.channel.purge(limit=amount + 1)

    # Checks current weather in city/country
    @commands.command()
    async def weather(self, ctx, *, city: str):
        "/weather city | I.E: /weather Phoenix"
        load_dotenv()
        owm = OWM(owmapi)
        mgr = owm.weather_manager()
        weather = mgr.weather_at_place(city + ", USA").weather
        temp_fahrenheit = weather.temperature('fahrenheit')["temp"]
        status = weather.detailed_status
        if temp_fahrenheit > 100:
            await ctx.send(f"The current temperature in {city} is {temp_fahrenheit} with {status}. Sappie should not go hiking.")
        else:
            await ctx.send(f"The current temperature in {city} is {temp_fahrenheit} with {status}. Get out there Sappie, this is approved hiking weather")


def setup(bot):
    bot.add_cog(TextFunctions(bot))
