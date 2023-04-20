import discord
from slash import *

@tree.command(name="calculadordesconto", description="Calcular o desconto de um produto")
async def calculardesconto(interaction, desconto: float, preço: float):
    des = (desconto/100)
    valordescontado = (preço * des)
    valorfinal = (preço - valordescontado)
    embed = discord.Embed(title="Calculador de desconto:",
    description=f"O preço sem desconto é: {preço} ",color=0x9208ea)
    embed.set_footer(text="Criado por Dimitri")
    embed.add_field(name="O valor do desconto é: ", value="{:.2f}".format(valordescontado), inline=False)
    embed.add_field(name="O valor final com desconto:", value="{:.2f}".format(valorfinal),inline=False)
    await interaction.response.send_message(embed = embed)