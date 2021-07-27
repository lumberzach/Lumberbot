import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
from dotenv import load_dotenv
import random
from twilio import twiml
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()


# Discord creds
token = os.getenv('disc_token')
guild = os.getenv('disc_guild')

app = Flask(__name__)


# Commands prefix
bot = commands.Bot(command_prefix=['/'])


@bot.event
async def on_ready():
    print('bot online.')


@app.route("/sms", methods=['GET', 'POST'])
async def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Your message has been received, thanks!")

    body = request.values.get('Body', None)
    print(body)

    return str(resp)


# Loads cogs
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


# Unloads cogs
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# Joins the Voice Channel the commanding user is in.
@bot.command(pass_context=True)
@commands.has_role("VIRGINS")
async def join(ctx):
    "Joins voice channel"
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients)

    if voice and voice.is_connected():
        await voice.disconnect()
        await voice.move_to(channel)
    else:
        await channel.connect()

    await ctx.send(f"Joined {channel}")


# Leaves the Voice Channel.
@bot.command(pass_context=True, aliases=['l'])
@commands.has_role("VIRGINS")
async def leave(ctx):
    "Leaves the voice channel"
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot is not in a Voice Channel")
        await ctx.send("I am not in a voice channel.")


@bot.command(pass_context=True)
async def vote(ctx):
    "starts a vote to move a member to crinkle town"


# Stops playing current mp3. Not possible to resume from a pause.
@bot.command(pass_context=True)
async def stop(ctx):
    "Stops current play function and will allow a new /play"
    voice = get(bot.voice_clients)
    voice.stop()


# Pauses current mp3, user can resume to continue.
@bot.command(pass_context=True)
async def pause(ctx):
    "Pauses current song, can be resumed with /resume"
    voice = get(bot.voice_clients)
    voice.pause()


# Resumes current mp3.
@bot.command(pass_context=True)
async def resume(ctx):
    "Resumes current song"
    voice = get(bot.voice_clients)
    voice.resume()


bot.run(token)
