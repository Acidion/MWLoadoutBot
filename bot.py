
#bot.py
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_LOADOUT_TOKEN')

bot = commands.Bot(command_prefix=':')

@bot.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    
@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    
@bot.command(name='test', help='Test message to test testing.')
async def test(ctx):
    response = 'Test Works'
    await ctx.send(response)
    
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
            
bot.run(TOKEN)
