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

@bot.command(name='vittoria', help='Lord Shaxx è fiero di te',pass_context=True)
async def positivo(context):
	paudiofile = [os.path.join(r,file) for r,d,f in os.walk("audio/vittoria") for file in f]
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
		await context.send('Non sei in un canale vocale!')

@bot.command(name='sconfitta', help='Lord Shaxx è deluso',pass_context=True)
async def sconfitta(context):
	paudiofile = [os.path.join(r,file) for r,d,f in os.walk("audio/sconfitta") for file in f]
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
		await context.send('Non sei in un canale vocale!')
		
@bot.command(name='parere', help='Lord Shaxx la pensa così',pass_context=True)
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
		await context.send('Non sei in un canale vocale!')

@bot.command(name='no', help='Si!',pass_context=True)
async def Yasss(context):
	channel=None
	channel = context.message.author.voice.channel
	if channel!= None:
		voc = await channel.connect()
		voc.play(discord.FFmpegPCMAudio('audio/Si.ogg'), after=lambda e: print('done', e))
		while voc.is_playing():
			await asyncio.sleep(1)
		voc.stop()
		await voc.disconnect()
	else:
		await context.send('Non sei in un canale vocale!')

bot.run('NzU5MDkwOTg3NTYwODYxNjk4.X24ckg.2ucH0GCirkLgT5wpJs-GTDWsnME')
