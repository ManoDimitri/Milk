import discord
from slash import *

@tree.command(name = "teste", description = "Testando o comando")
async def teste(interaction):
    server_id = interaction.guild_id

    await interaction.response.send_message("Visão, eu to online")