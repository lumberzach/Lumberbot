import discord
from discord.ext import commands
from discord.utils import get
from random import randint
import os
import random
from twilio.rest import Client
from dotenv import load_dotenv



load_dotenv()

# Account SID and Auth Token from Twilio account stored in dotenv file
account_sid = os.getenv('sid')
auth_token = os.getenv('token')

# Phone numbers stored in dotenv file
zach_sms = os.getenv('zach_sms')
gale_sms = os.getenv('gale_sms')
gadola_sms = os.getenv('gadola_sms')
eugene_sms = os.getenv('eugene_sms')
sappie_sms = os.getenv('sappie_sms')
colby_sms = os.getenv('colby_sms')



class SmsCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # Sends SMS to a specified user from the discord channel
    @commands.command()
    @commands.has_role("VIRGINS")
    async def text(self, ctx, name: str, *, text_out: str):
        "Texts a user, format is: /text name message I.E: /text zach hey get on for a game"
        try:
            client = Client(account_sid, auth_token)
            phone_bank = {"zach": zach_sms,
                          "gale": gale_sms,
                          "gadola": gadola_sms,
                          "eugene": eugene_sms,
                          "sappie": sappie_sms
                          }
            name = name
            number = phone_bank.get(name.lower())
            text_out = text_out

            message = client.messages.create(
                to=number,
                from_="+12566678863",
                body=text_out + "\nYou can't respond to this message")

            print(message.sid)
            await ctx.send(f"SMS successfuly sent to {name.capitalize()}")
        except:
            await ctx.send(f"There was an error, format should be /text zach hey get on for a game")


def setup(bot):
    bot.add_cog(SmsCommand(bot))
