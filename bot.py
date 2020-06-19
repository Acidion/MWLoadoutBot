#bot.py
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_LOADOUT_TOKEN')
JSON_FILE = os.getenv('JSON_FILE_NAME')

bot = commands.Bot(command_prefix='$')
'''Declare and preload JSON file on bot load'''

def loadJSON():
    try:
        with open(JSON_FILE) as f:
            data = json.load(f)
        return json.loads(data)
    except FileNotFoundError:
        return []
    
def saveJSON():
    with open(JSON_FILE, 'w') as f:
        json.dump(loadouts, f)
    loadouts = loadJSON

@bot.event
async def on_ready():
    print('{} has connected to Discord!'.format(bot.user.name))
    
@bot.command(name='test', help='Test message to test testing.')
async def test(ctx):
    response = 'Test Works'
    await ctx.send(response)

@bot.command(name='addload', help='Add a loadout. Usage $addload <name> <BaseGun> <attach1> <attach2> <attach3> <attach4> <attach5>')
async def add(ctx, *args):
    addedby = ctx.user.name
    loadoutName = args[0]
    baseGun = args[1]
    attach1 = args[2]
    attach2 = args[3]
    attach3 = args[4]
    attach4 = args[5]
    attach5 = args[6]
    temploadout = {
        "addedby":addedby,
        "loadoutName":loadoutName,
        "basegun":baseGun,
        "attachments": ( attach1, attach2, attach3, attach4, attach5)
    }
    print(temploadout)

    exists = False
    response = ''
    if loadouts:
        for l in loadouts:
            if l["loadoutName"] == loadoutName:
                exists = True
    if not exists:
        with open(JSON_FILE, 'w') as outfile:
            response = 'Loadout {} added to repository.'.format(loadoutName)
    else:
        response = 'Loadout {} already exists.'.format(loadoutName)

    await ctx.send(resposne)
    
@bot.command(name='deleteload', help='Remove a loadout. Usage $deleteload <name>')
async def delete(ctx, *args):
    loadoutName = args[1]
    response = ''
    if ctx.author.name != loadout[index]["addedby"]:
        response = 'You can\'t remove {}, as you did not add it.'.format(args[0])
    else:
        for idx, item in loadouts: 
            if item["loadoutName"] == loadoutName:
                loadouts.pop(idx)
                response = 'Loadout {} removed from repository.'.format(args[0])
                saveJSON
        
    await ctx.send(response)
   
@bot.command(name='getload', help='Gets details of requested loadout. Usage $getload <name>')
async def get(ctx, args):
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

            
loadouts = loadJSON()
bot.run(TOKEN)
