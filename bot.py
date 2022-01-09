import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix = "?")

bot.lava_nodes = [
  {
    'host': 'lava.link',
    'port': 80,
    'rest_uri': f'http://lava.link:80',
    'identifier': 'MAIN',
    'password': 'anything',
    'region': 'canada'
  }
]

@bot.event
async def on_ready():
  print("Bot is ready to play music.")
  bot.load_extension('dismusic')

keep_alive()
bot.run(os.getenv('TOKEN'))