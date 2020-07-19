import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
from dotenv import load_dotenv
import random

load_dotenv()

token = os.getenv('disc_token')
guild = os.getenv('disc_guild')

bot = commands.Bot(command_prefix=['/'])


# cogs
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


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
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await ctx.send(f"Joined {channel}")


# Leaves the Voice Channel.
@bot.command(pass_context=True, aliases=['l'])
@commands.has_role("VIRGINS")
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot is not in a Voice Channel")
        await ctx.send("I am not in a voice channel.")


# Stops playing current mp3. Not possible to resume from a pause.
@bot.command(pass_context=True)
async def stop(ctx):
    voice = get(bot.voice_clients)
    voice.stop()



# Pauses current mp3, user can resume to continue.
@bot.command(pass_context=True)
async def pause(ctx):
    voice = get(bot.voice_clients)
    voice.pause()


# Resumes current mp3.
@bot.command(pass_context=True)
async def resume(ctx):
    voice = get(bot.voice_clients)
    voice.resume()


# Removes existing mp3 and downloads new mp3 from youutube, renames to song.mp3, streams song to voice
@bot.command(pass_context=True, aliases=['p'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting everything ready now")

    voice = get(bot.voice_clients)

    # options for audio quality ect.
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")

    #add volume control loop here or where?


bot.run(token)
