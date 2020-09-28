# bot.py
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='Shaxx ')

@bot.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

@bot.command(name='positivo', help='Lord Shaxx è fiero di te',pass_context=True)
async def positivo(context):
	paudiofile = os.scandir('audio/positive/')
	pselectedaudio = random.choice(paudiofile)
	user=context.message.author
	voice_channel=user.voice.voice_channel
	channel=None
	if voice_channel!= None:
		channel=voice_channel.name
		await client.say('User is in channel: '+ channel)
		vc= await client.join_voice_channel(voice_channel)
		player = vc.create_ffmpeg_player(pselectedaudio, after=lambda: print('done'))
		player.start()
		while not player.is_done():
			await asyncio.sleep(1)
			player.stop()
		await vc.disconnect()
	else:
		await client.say('Non sei in un canale vocale!')

bot.run('NzU5MDkwOTg3NTYwODYxNjk4.X24ckg.2ucH0GCirkLgT5wpJs-GTDWsnME')
