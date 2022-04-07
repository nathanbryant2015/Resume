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


#Need to finish testing and coding here. This is for Mute
@bot.command(description= "Mutes the specified user.")
#@commands.has_permissions(manage_message=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=True, read_messages=True)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")


#Need to finish testing and coding here. This is for unmute
@bot.command(description= "Unmutes a specified user.")
#@commands.has_permissions(manage_message=True)
async def unmute(ctx, Member: discord.Member):
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"you were unmuted in the server {guild.name}")

client.run(TOKEN)
