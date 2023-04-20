import discord
from slash import *
from main import server_id

@tree.command(name = "teste", description = "Testando o comando",guild=discord.Object(id=server_id))
async def teste(interaction):
    await interaction.response.send_message("Visão, eu to online")