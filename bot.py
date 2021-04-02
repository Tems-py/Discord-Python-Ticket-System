from discord.ext import commands

import asyncpg
import discord
import os
import json

# get token
with open ("data.json", "r") as f:
    data = json.load(f)
    token = data["token"]
    db_pswd = data["db_pwd"]

# DB Connection
async def create_db_pool():
    client.db = await asyncpg.create_pool(database="PostgreSQL-Tickets", user="postgres", password=db_pswd)

# definition
intents = discord.Intents().all()
client = commands.Bot(command_prefix="?", intents=intents, help_command=None, case_insensitive=True)
guild = discord.Guild

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("----------------------------------------")
 
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"a system"))
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                client.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename}')
            except Exception as e:
                print(f'Failed to load {filename}')
                print(f'[ERROR] {e}')

    print("----------------------------------------")

client.loop.run_until_complete(create_db_pool())
client.run(token)
