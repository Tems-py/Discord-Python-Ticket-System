import discord
import asyncio
import os
import urllib.parse, urllib.request, re

from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure

# definition
intents = discord.Intents().all()
client = commands.Bot(command_prefix = '?',intents=intents, help_command=None)
guild = discord.Guild

# token file
token = open("token.txt").read()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("----------------------------------------")
    await client.change_presence(activity=discord.Game(name='...'))

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                client.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename}')
            except Exception as e:
                print(f'Failed to load {filename}')
                print(f'[ERROR] {e}')
    print("----------------------------------------")

    
client.run(token)
