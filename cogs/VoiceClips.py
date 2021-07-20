import discord
from discord.ext import commands
from discord.utils import get
from random import randint
import os
import random


class VoiceClips(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # Plays a random sound clip from shortclip folder.
    @commands.command(pass_context=True)
    async def clip(self, ctx):
        basedir = r"C:/Users/Boxca/PycharmProjects/Lumberbot/shortclips/"
        randomfile = random.choice(os.listdir(basedir))
        path = basedir + randomfile
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play getfucked.mp3 clip
    @commands.command(pass_context=True, aliases=['gfd'])
    async def gf(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\sappie\gfd.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play moncler.mp3 clip
    @commands.command(pass_context=True)
    async def moncler(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\savage\moncler.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = .5

    ###Quotes###
    # Play practice.mp3 clip
    @commands.command(pass_context=True)
    async def practice(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\quotes\practice.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 2

    @commands.command(pass_context=True)
    async def beat(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\quotes\beat.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 2

    @commands.command(pass_context=True)
    async def allday(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\quotes\allday.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 2

    @commands.command(pass_context=True)
    async def beat2(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\quotes\beat3.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 2


    # Colby Clips
    # Play snarb.mp3 clip
    @commands.command(pass_context=True, aliases=['delusional', 'thedefeated', "masta bruce", "bruce"])
    async def bb(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\snarb\snarb.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play snarb2.mp3 clip
    @commands.command(pass_context=True, aliases=['fellas'])
    async def mclovin(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\snarb\snarb2.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    @commands.command(pass_context=True)
    async def fcolby(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\shortclips\efcolby.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play nuts.mp3 clip
    @commands.command(pass_context=True)
    async def nuts(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\shortclips\nuts.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play ree.mp3 clip
    @commands.command(pass_context=True, aliases=['re'])
    async def ree(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\shortclips\ree.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play mike.mp3 clip
    @commands.command(pass_context=True)
    async def mike(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\snarb\mike.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play sappie.mp3 clip
    @commands.command(pass_context=True, aliases=['sap'])
    async def sappie(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\sappie\sappie.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1



    # Play sappie.mp3 clip
    @commands.command(pass_context=True)
    async def hype2(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\sappie\hype.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play ass.mp3 clip
    @commands.command(pass_context=True)
    async def ass(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\shortclips\ass.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play eug.mp3 clip
    @commands.command(pass_context=True)
    async def eug(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\eug\eug.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 3.0

    # Play circuits.mp3 clip
    @commands.command(pass_context=True, aliases=['hype'])
    async def circuits(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\circuits\circuits.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play circuits2.mp3 clip
    @commands.command(pass_context=True, aliases=['lol'])
    async def thejoker(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\circuits\circuits2.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play Gadola shortcake.mp3 clip
    @commands.command(pass_context=True, aliases=['gadola'])
    async def shortcake(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\gadola\shortcake.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1


    # Play Gadola tna.mp3 clip
    @commands.command(pass_context=True)
    async def tna(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\gadola\tna.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = .5

    # Play niceshot.mp3 clip
    @commands.command(pass_context=True, aliases=['ns'])
    async def niceshot(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\gadola\niceshot.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

    # Play omg.mp3 clip
    @commands.command(pass_context=True)
    async def omg(self, ctx):
        path = r"C:\Users\Boxca\PycharmProjects\Lumberbot\shortclips\omg.mp3"
        voice = get(self.bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(path), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1


def setup(bot):
    bot.add_cog(VoiceClips(bot))
