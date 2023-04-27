import discord
from slash import *

@tree.command(name = "teste", description = "Testando o comando")
async def teste(interaction):   
    await interaction.response.send_message("Visão, eu to online")