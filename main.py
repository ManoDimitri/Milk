import discord
import os
from dotenv import load_dotenv
from commands import teste, calculadordesconto, equacao, geradorcpf, validadorcpf, calcular
from slash import tree, client, intents

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print("O bot está online.")
    

client.run(discord_token)
