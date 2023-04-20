import discord
from slash import *

@tree.command(name="calcular", description="Cálculos básicos")
async def calcular(interaction, valor: str):
    server_id = interaction.guild_id
    try:
        resposta = eval(valor)
    except:
        await interaction.response.send_message("Desculpe, a expressão inserida é inválida.")
        return
    await interaction.response.send_message(f"A resposta é: {resposta}")
