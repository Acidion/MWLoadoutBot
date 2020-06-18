
#bot.py
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_LOADOUT_TOKEN')

bot = commands.Bot(command_prefix='$')
'''Declare and preload JSON file on bot load'''

@bot.event
async def on_ready():
    print('{} has connected to Discord!'.format(bot.user.name))
    
@bot.command(name='test', help='Test message to test testing.')
async def test(ctx):
    response = 'Test Works'
    await ctx.send(response)

@bot.command(name='addload', help='Add a loadout. Usage $addload <name> <BaseGun> <attach1> <attach2> <attach3> <attach4> <attach5>'
async def add(ctx, *args):
    addedby = ctx.user.name
    loadoutName = args[0]
    baseGun = args[1]
    attach1 = args[2]
    attach2 = args[3]
    attach3 = args[4]
    attach4 = args[5]
    attach5 = args[6]
    loadout = {
        "addedby":addedby,
        "loadoutName":loadoutName,
        "basegun":baseGun,
        "attachments": ( attach1, attach2, attach3, attach4, attach5)
    }
    """Check if loadout exists in stored loadouts for update purposes
       Add to JSON and refresh locally held array of loadouts"""
    response = 'Loadout {} added to repository.'.format(args[0])
    await ctx.send(resposne)
    
@bot.command(name='deleteload', help='Remove a loadout. Usage $deleteload <name>')
async def del(ctx, *args):
    """Check if the referenced loadout exists and if it was added by the user invoking command"""
    """Do the removal of the loadout from the json and the locally held array"""
    if ctx.author.name != loadout[index]["addedby"]:
        response = 'You can\'t remove {}, as you did not add it.'.format(args[0])
    response = 'Loadout {} removed from repository.'.format(args[0])
    await ctx.send(response)
   
@bot.command(name='getload', help='Gets details of requested loadout. Usage $getload <name>')
aync def get(ctx, args):
    """Look through list of loadouts for user argument and return the values if found"""
    response = 'Loadout not found.'
    await ctx.send(response)
             
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write('Unhandled message: {}\n'.format(args[0]))
        else:
            raise
            
bot.run(TOKEN)
