
#bot.py
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_LOADOUT_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('{} has connected to Discord!'.format(bot.self))

    
@bot.event
async def on_message(message):
    if message.author == bot.self:
        return
    
@bot.command(name='test', help='Test message to test testing.')
async def test(ctx):
    response = 'Test Works'
    await ctx.send(response)
    
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write('Unhandled message: {}\n'.format(args[0]))
        else:
            raise
            
bot.run(TOKEN)
