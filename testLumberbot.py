import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import time
from dotenv import load_dotenv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

token = os.getenv('disc_token')
guild = os.getenv('disc_guild')

bot = commands.Bot(command_prefix=['/'])


@bot.command(pass_context=True, Alases="Hulu")
async def hulu(ctx):
    await ctx.send("Launching hulu... please wait until prompted to search")

    # loading webdrivers and opening the website
    options = Options()
    # Path to your chrome profile
    options.add_argument("user-data-dir=C:\\Users\\Boxca\\AppData\\Local\\Google\\Chrome\\profiletwo")
    driver = webdriver.Chrome(r"C:\Users\Boxca\Downloads\Drivers\chromedriver_win32 (1)\chromedriver.exe", options=options)
    driver.get('https://www.hulu.com/')

    time.sleep(5)

    # sign in
    try:
        element = driver.find_element_by_class_name('navigation__login-button').click()
        print("We are logging in")
        email = driver.find_element_by_id('email_id')
        password = driver.find_element_by_id('password_id')
        login_button = driver.find_element_by_xpath("//button[@class='jsx-1761454348 login-button']")

        email.send_keys('boxcarracer0110@hotmail.com')
        password.send_keys('pn1567')
        login_button.click()

        time.sleep(5)

        try:
            # closing the modals
            welcome = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "WelcomeModal__cta"))
            )
            welcome.click()

            time.sleep(2)
            print("Ready to search hulu")

        except NoSuchElementException:
            print("Ready to search hulu")



        print("Ready to search hulu")
    except NoSuchElementException:
        print("Ready to search hulu")






# cogs load command
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# Plays a random sound clip from shortclip folder.
@bot.command(pass_context=True)
async def clip(ctx):
    basedir = r"C:/Users/Boxca/PycharmProjects/Lumberbot/shortclips/"
    randomfile = random.choice(os.listdir(basedir))
    path = basedir + randomfile
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1





# Delete text channel messages, 5 is default if no amount is given.
@bot.command(pass_context=True)
@commands.has_role("VIRGINS")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


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



# Play moncler.mp3 clip
@bot.command(pass_context=True)
async def moncler(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\savage\moncler.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = .5


# Play practice.mp3 clip
@bot.command(pass_context=True)
async def practice(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\quotes\practice.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 2


#Colby Clips
# Play snarb.mp3 clip
@bot.command(pass_context=True, aliases=['delusional', 'thedefeated', "masta bruce", "bruce"])
async def bb(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\snarb\snarb.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


# Play snarb2.mp3 clip
@bot.command(pass_context=True, aliases=['fellas'])
async def mclovin(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\snarb\snarb2.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


# Play ree.mp3 clip
@bot.command(pass_context=True, aliases=['re, ree'])
async def re(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\snarb\snarb2.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


# Play mike.mp3 clip
@bot.command(pass_context=True)
async def mike(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\snarb\mike.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


# Play sappie.mp3 clip
@bot.command(pass_context=True, aliases=['sap'])
async def sappie(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\sappie\sappie.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1





# Play sappie.mp3 clip
@bot.command(pass_context=True)
async def hype2(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\sappie\hype.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


# Play eug.mp3 clip
@bot.command(pass_context=True, aliases=['gay'])
async def eug(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\eug\eug.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 3.0


# Play circuits.mp3 clip
@bot.command(pass_context=True, aliases=['hype'])
async def circuits(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\circuits\circuits.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


# Play circuits2.mp3 clip
@bot.command(pass_context=True, aliases=['lol'])
async def thejoker(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\circuits\circuits2.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


# Play Gadola rage.mp3 clip
@bot.command(pass_context=True, aliases=['gadola'])
async def rage(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\gadola\rage.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


# Play Gadola tna.mp3 clip
@bot.command(pass_context=True)
async def tna(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\gadola\tna.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = .5


# Play niceshot.mp3 clip
@bot.command(pass_context=True, aliases=['ns'])
async def niceshot(ctx):
    path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\gadola\niceshot.mp3"
    voice = get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1


bot.run(token)