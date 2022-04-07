#The BAT file will keep the code running.

# Discord Bot modules
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

#Random for 8 Ball
import random


#Tokens 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Discord Client (User)
client = discord.Client()

#Discord chat symbol to call to the bot
bot = commands.Bot(command_prefix='!')



#Event prints the active users once the bot starts. This ensures the bot was started successfully.
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


#Executes the 8 Ball command if the user tytpes !8ball
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    ball = [
        "Don't Count on it",
        "My Reply is no",
        "Outlook good",
        "All signs point to yes",
        "Ask again later"
]

    if message.content == '8ball':
        response = random.choice(ball)
        print(response)
        await message.channel.send(response)

client.run(TOKEN)
