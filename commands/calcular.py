import discord
from slash import *

@tree.command(name="calcular", description="Cálculos básicos",guild=discord.Object(id=714557909878571119))
async def calcular(interaction, valor: str):
    try:
        resposta = eval(valor)
    except:
        await interaction.response.send_message("Desculpe, a expressão inserida é inválida.")
        return
    await interaction.response.send_message(f"A resposta é: {resposta}")
