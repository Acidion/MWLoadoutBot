#bot.py
import os
import json
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
TOKEN = os.getenv('DISCORD_LOADOUT_TOKEN')
JSON_FILE = os.getenv('JSON_FILE_NAME')

bot = commands.Bot(command_prefix='$')
'''Declare and preload JSON file on bot load'''

def loadJSON():
    try:
        mypath = Path(JSON_FILE)
        if mypath.stat().st_size != 0:
            with open(JSON_FILE) as f:
                data = json.load(f)
            return data
    except FileNotFoundError:
        return []
    
def saveJSON():
    with open(JSON_FILE, 'w') as f:
        print("Saving following loadouts:" + loadouts)
        json.dump(loadouts, f)
    loadouts = loadJSON()

def search(name):
    result = False
    if loadouts:
        print("Loadout Data: " + loadouts)
        for load in loadouts:
            print("Search Load Item: " + load)
            if load["loadoutName"] == name:
                result = True
    return result

@bot.event
async def on_ready():
    print('{} has connected to Discord!'.format(bot.user.name))
    
@bot.command(name='test', help='Test message to test testing.')
async def test(ctx):
    response = 'Test Works'
    await ctx.send(response)

@bot.command(name='addload', help='Add a loadout.\n Usage $addload <name> <BaseGun> <attach1> <attach2> <attach3> <attach4> <attach5>')
async def add(ctx, *args):
    addedby = ctx.message.author.name
    loadoutName = args[0]
    baseGun = args[1]
    attach1 = args[2]
    attach2 = args[3]
    attach3 = args[4]
    attach4 = args[5]
    attach5 = args[6]
    temploadout = { "loadout": [
        { "addedby":addedby,
        "loadoutName":loadoutName,
        "basegun":baseGun,
        "attachments": ( attach1, attach2, attach3, attach4, attach5) }
        ]
    }
    print(temploadout)

    exists = search(loadoutName)
    response = ''
    
    if not exists:
        loadouts.append(temploadout)
        saveJSON()
        response = 'Loadout {} added to repository.'.format(loadoutName)
    else:
        response = 'Loadout {} already exists.'.format(loadoutName)

    await ctx.send(response)
    
@bot.command(name='deleteload', help='Remove a loadout. Usage $deleteload <name>')
async def delete(ctx, *args):
    loadoutName = args[0]
    response = ''
    for loadout in loadouts:
        if ctx.message.author.name != loadout["addedby"]:
            response = 'You can\'t remove {}, as you did not add it.'.format(args[0])
    if response == '':
        for idx, item in loadouts: 
            if item["loadoutName"] == loadoutName:
                loadouts.pop(idx)
                response = 'Loadout {} removed from repository.'.format(args[0])
                saveJSON
        
    await ctx.send(response)
   
@bot.command(name='getload', help='Gets details of requested loadout. Usage $getload <name>')
async def get(ctx, args):
    """Look through list of loadouts for user argument and return the values if found"""
    loadoutName = args[0]
    for load in loadouts:
        if load["loadoutName"]==loadoutName:
            response = 'Name: {0} Base Gun: {1} Attachments: {2} {3} {4} {5} {6} Added By: {7}'.format(loadoutName, load["baseGun"], load["attachments"][0], load["attachments"][1], load["attachments"][2], load["attachments"][3], load["attachments"][4], load["addedBy"])
            print(response)
        else:
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
