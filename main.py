import discord
import os
from dotenv import load_dotenv
from commands import teste, calculadordesconto, equacao, geradorcpf, validadorcpf, calcular
from slash import tree, client, intents

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')


@client.event
async def on_ready():
   print("Estou conectado!")

@tree.command(name="id", description="Pegar o ID")
async def id(interaction):
    guild_id = interaction.guild.id
    print(f"O ID do servidor é {guild_id}")
    

client.run(discord_token)
