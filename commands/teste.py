import discord
from slash import *
from main import server_id

@tree.command(name="teste", description="Testando o comando")
async def teste(interaction):
    server_id = interaction.guild_id
    await interaction.response.send_message(f"Estou online no servidor com ID {server_id}!")