import discord
import os
from dotenv import load_dotenv
from commands import teste, calculadordesconto, equacao, geradorcpf, validadorcpf, calcular
from slash import intents, client, tree

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    guild = client.guilds[0]
    await tree.sync(guild=guild)
    print(f"Eu entrei como {client.user.name} na guild {guild.name}")

    await client.change_presence(status= discord.Status.online,)
    

client.run(discord_token)
