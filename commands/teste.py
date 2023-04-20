import discord
from slash import *
from main import server_ids

@tree.command(name="teste", description="Testando o comando")
async def teste(interaction):
    await interaction.response.send_message("Estou online no servidor!")