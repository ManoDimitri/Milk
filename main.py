import discord
import os
from dotenv import load_dotenv
from commands import teste, calculadordesconto, equacao, geradorcpf, validadorcpf, calcular
from slash import tree, client, intents

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
guilds = client.guilds

@client.event
async def on_ready():
   print("Estou conectado!")
    

client.run(discord_token)
