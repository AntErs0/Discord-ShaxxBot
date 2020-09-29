# bot.py
import os
import discord
import random
import asyncio
from dotenv import load_dotenv
from discord import ext
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='Shaxx ')

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

@bot.command(name='positive', help='Lord Shaxx  is pleased with you',pass_context=True)
async def positivo(context):
	paudiofile = [os.path.join(r,file) for r,d,f in os.walk("audio/positive") for file in f]
	channel=None
	channel = context.message.author.voice.channel
	if channel!= None:
		voc = await channel.connect()
		voc.play(discord.FFmpegPCMAudio(random.choice(paudiofile)), after=lambda e: print('done', e))
		while voc.is_playing():
			await asyncio.sleep(1)
		voc.stop()
		await voc.disconnect()
	else:
		await context.send('You are not in a voice channel!')

@bot.command(name='negative', help='Lord Shaxx is disappointed',pass_context=True)
async def sconfitta(context):
	paudiofile = [os.path.join(r,file) for r,d,f in os.walk("audio/negative") for file in f]
	channel=None
	channel = context.message.author.voice.channel
	if channel!= None:
		voc = await channel.connect()
		voc.play(discord.FFmpegPCMAudio(random.choice(paudiofile)), after=lambda e: print('done', e))
		while voc.is_playing():
			await asyncio.sleep(1)
		voc.stop()
		await voc.disconnect()
	else:
		await context.send('You are not in a voice channel!')
		
@bot.command(name='thought', help='Random message',pass_context=True)
async def sconfitta(context):
	paudiofile = [os.path.join(r,file) for r,d,f in os.walk("audio/") for file in f]
	channel=None
	channel = context.message.author.voice.channel
	if channel!= None:
		voc = await channel.connect()
		voc.play(discord.FFmpegPCMAudio(random.choice(paudiofile)), after=lambda e: print('done', e))
		while voc.is_playing():
			await asyncio.sleep(1)
		voc.stop()
		await voc.disconnect()
	else:
		await context.send('You are not in a voice channel!')

@bot.command(name='no', help='Yassss!',pass_context=True)
async def Yasss(context):
	channel=None
	channel = context.message.author.voice.channel
	if channel!= None:
		voc = await channel.connect()
		voc.play(discord.FFmpegPCMAudio('audio/Yas.mp3'), after=lambda e: print('done', e))
		while voc.is_playing():
			await asyncio.sleep(1)
		voc.stop()
		await voc.disconnect()
	else:
		await context.send('You are not in a voice channel!')

bot.run(os.getenv('DISCORD_TOKEN'))
