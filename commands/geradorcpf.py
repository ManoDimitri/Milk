import discord
from slash import *
from cpf_generator import CPF

@tree.command(name="geradorcpf", description="Vai gerar um CPF")
async def geradorcpf(interaction):
    cpf = CPF.generate()
    formatedcpf = CPF.format(cpf)
    await interaction.response.send_message(f"CPF: {formatedcpf}")