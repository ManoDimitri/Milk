import discord
from slash import *
from cpf_generator import CPF

@tree.command(name="validadorcpf", description="Valida o CPF informado, informa o cpf sem os . e -",guild=discord.Object(id=714557909878571119))
async def validadorcpf(interaction, cpf: str):
    fcpf = CPF.format(cpf)
    validadorcpf = CPF.validate(fcpf)
    if validadorcpf == True:
        await interaction.response.send_message(f"O CPF: {fcpf} é verdadeiro!")
    elif validadorcpf == False:
        await interaction.response.send_message(f"O CPF: {fcpf} é falso!")