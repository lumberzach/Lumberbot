import discord
from discord.ext import commands
from discord.utils import get
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import youtube_dl
import os
import pyautogui
import time


class YoutubeStreaming(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Delete text channel messages, 5 is default if no amount is given.
    @commands.command(pass_context=True)
    @commands.has_role("VIRGINS")
    async def yt(self, ctx):




        # Open Chrome
        options = Options()
        options.add_argument("user-data-dir=C:\\Users\\Boxca\\AppData\\Local\\Google\\Chrome\\profiletwo")

        global driver

        driver = webdriver.Chrome(r"C:\Users\Boxca\Downloads\Drivers\chromedriver_win32 (1)\chromedriver.exe",
                                  options=options)

        # Stream the youtube video or just play audio in discord channel.

        await ctx.send("Press 1 for a Video Stream, 2 for only audio")
        msg = await self.bot.wait_for('message')
        choice = int(msg.content)
        if choice < 2:
            # Start stream from Discord
            pyautogui.click(pyautogui.locateCenterOnScreen('startstream.png'))
            time.sleep(2.2)
            pyautogui.click(pyautogui.locateCenterOnScreen('screen.png'))
            time.sleep(2.3)
            pyautogui.click(pyautogui.locateCenterOnScreen('golive.png'))

            # Search YouTube from user's input from discord
            await ctx.send("What are we searching for?")
            msg = await self.bot.wait_for('message')
            search_query = msg.content
            driver.get("https://www.youtube.com/results?search_query=" + search_query)

            # Enumerate through results, breaks after 3.
            for num, element in enumerate(driver.find_elements_by_id("video-title"), start=1):
                await ctx.send(f"Enter {num} for {element.text}")
                if num == 3:
                    break

            # Take user's choice and start video + return url
            await ctx.send("Please enter choice from 1-3")
            msg = await self.bot.wait_for("message")
            choice = int(msg.content)
            if choice <= 3:
                driver.find_elements_by_id('video-title')[choice - 1].click()

        else:
            # Search YouTube from user's input from discord
            await ctx.send("What are we searching for?")
            msg = await self.bot.wait_for('message')
            search_query = msg.content
            driver.get("https://www.youtube.com/results?search_query=" + search_query)

            # Enumerate through results, breaks after 3.
            for num, element in enumerate(driver.find_elements_by_id("video-title"), start=1):
                await ctx.send(f"Enter {num} for {element.text}")
                if num == 3:
                    break

            # Take user's choice and start video + return url
            await ctx.send("Please enter choice from 1-3")
            msg = await self.bot.wait_for("message")
            choice = int(msg.content)
            if choice <= 3:

                element = driver.find_elements_by_id('video-title')[choice - 1]
                url = element.get_attribute('href')
                print(url)
                driver.quit()

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

                voice = get(self.bot.voice_clients)

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

    @commands.command(pass_context=True)
    @commands.has_role("VIRGINS")
    async def ytstop(self, ctx):
        driver.quit()


def setup(bot):
    bot.add_cog(YoutubeStreaming(bot))
