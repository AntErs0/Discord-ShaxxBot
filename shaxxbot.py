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

@bot.command(name='positivo', help='Lord Shaxx è fiero di te',pass_context=True)
async def positivo(context):
	paudiofile = os.listdir('audio/positive/')
	channel=None
	channel = context.message.author.voice.channel
	if channel!= None:
		vc = channel.name
		await context.send('User is in channel: '+ vc)
		voc = await channel.connect()
		voc.play(discord.FFmpegPCMAudio('audio/positive/' + random.choice(paudiofile)), after=lambda e: print('done', e))
		while voc.is_playing():
			await asyncio.sleep(1)
			voc.stop()
		await voc.disconnect()
	else:
		await context.send('Non sei in un canale vocale!')

bot.run('NzU5MDkwOTg3NTYwODYxNjk4.X24ckg.2ucH0GCirkLgT5wpJs-GTDWsnME')
