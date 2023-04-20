import discord
from slash import *

@tree.command(name = "teste", description = "Testando o comando",guild=discord.Object(id=714557909878571119))
async def teste(interaction):

    await interaction.response.send_message("Visão, eu to online")