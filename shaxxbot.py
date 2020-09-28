# bot.py
import os

import discord
from dotenv import load_dotenv
import random
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



@bot.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
    
@bot.event
async def on_message(message):
	if message.author == client.user:
		return

	brooklyn_99_quotes = [
		'I\'m the human form of the 💯 emoji.',
		'Bingpot!',
		(
		'Cool. Cool cool cool cool cool cool cool, '
		'no doubt no doubt no doubt no doubt.'
		),
	]

	if message.content == '99!':
		response = random.choice(brooklyn_99_quotes)
		await message.channel.send(response)

client.run('NzU5MDkwOTg3NTYwODYxNjk4.X24ckg.2ucH0GCirkLgT5wpJs-GTDWsnME')