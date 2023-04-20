import discord
import os
from dotenv import load_dotenv
from commands import teste, calculadordesconto, equacao, geradorcpf, validadorcpf, calcular
from slash import tree, client, intents

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready(interaction):
    server_id = interaction.guild.id
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')
    print('------')
    activity = discord.Activity(name='Testando bot', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)
    

client.run(discord_token)
