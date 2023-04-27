import discord
from slash import *
from main import guilds

@tree.command(name = "teste", description = "Testando o comando", guild=discord.Object(id=guilds))
async def teste(interaction):   
    await interaction.response.send_message("Visão, eu to online")