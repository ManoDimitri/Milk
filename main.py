import discord
import os
from dotenv import load_dotenv
from commands import teste, calculadordesconto, equacao, geradorcpf, validadorcpf, calcular
from slash import tree, client, intents

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

server_ids = []

@client.event
async def on_ready():
    global server_ids  
    server_ids = [guild.id for guild in client.guilds]

@tree.command()
async def meucomando(ctx):
    guild_id = ctx.guild.id
    print(f"O ID do servidor é {guild_id}")
    

client.run(discord_token)
