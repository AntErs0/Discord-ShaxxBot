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
prefix = os.getenv('COMMAND_PREFIX')
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')
	
@bot.command(name="help" , pass_contex = True)
async def help(context):    
	embed = discord.Embed(colour = discord.Colour.from_rgb(255, 0, 0))
	embed.set_author(name="Richiama Lord Shaxx con \"" + prefix + "\" seguito da uno dei seguenti comandi:")
	embed.add_field(name="vittoria" , value= "Lord Shaxx è fiero di te" , inline=False)
	embed.add_field(name="sconfitta" , value= "Lord Shaxx è deluso" , inline=False)
	embed.add_field(name="parere" , value= "Lord Shaxx la pensa così" , inline=False)
	embed.add_field(name="no" , value= "SI!" , inline=False)
	await context.send(embed=embed)

@bot.command(name='vittoria',pass_context=True)
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

@bot.command(name='sconfitta',pass_context=True)
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
		
@bot.command(name='parere',pass_context=True)
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

@bot.command(name='no',pass_context=True)
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

bot.run(os.getenv('DISCORD_TOKEN'))
