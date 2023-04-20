import discord
from slash import *
from math import sqrt

@tree.command(name = "equação", description = "Calcular equação do segundo grau",guild=discord.Object(id=714557909878571119))
async def equação(interaction, a: int, b: int, c: int):
    delta = b**2 - 4*a*c
    if a == 0:
        await interaction.response.send_message("Se a = 0, não é uma equação do segundo grau. Execute o comando novamente em que o valor de A seja diferente de 0.")
    elif delta < 0:
        await interaction.response.send_message(f"O valor de delta é menor que 0, a equação não apresentará raízes. Valor de delta: {delta}")
    else:
        raiz = sqrt (delta)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b -raiz) / (2 * a)
        embed = discord.Embed(title="Equação do segundo grau:",
        description=f"O valor de a: {a} b: {b} c: {c} ",color=0x9208ea)
        embed.set_footer(text="Criado por Dimitri")
        embed.add_field(name="O valor de delta é:", value="{:.2f}".format(delta), inline=False)
        embed.add_field(name="O valor da raiz de delta é:", value="{:.2f}".format(raiz),inline=False)
        embed.add_field(name="O valor de x1:", value="{:.2f}".format(x1),inline=False)
        embed.add_field(name="O valor de x2:", value="{:.2f}".format(x2),inline=False)
        await interaction.response.send_message(embed = embed)