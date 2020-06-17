
#bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_LOADOUT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('{client.user} has connected to Discord!')

client.run(TOKEN)

