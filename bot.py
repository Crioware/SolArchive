import time
import discord
import logging
from discord.ext import commands
from discord_ui import UI, SlashOption

tokenfile = open('#Important/token.txt')
TOKEN = tokenfile.read()
bot = commands.Bot("")
ui = UI(bot)

# Deforestation is a major problem in the programming community
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='#Important/discordlogging.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# Sends confirmation that it is online to the console
@bot.event
async def on_ready():
    logon = 'Logged on as {0.user} at '.format(bot) + time.strftime('%X') + ' ' + time.strftime('%x')
    print(logon)
    # TODO: Update the presence with a useful message at some point
    await bot.change_presence(activity=discord.Game(name='Hey Alex, please change this later!'))