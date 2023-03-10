import discord
from discord import app_commands
from math import sqrt
import os
from dotenv import load_dotenv
from cpf_generator import CPF

discord_token = os.getenv('TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=874833976085344307))
    print(f"Eu entrei como {client.user.name}")

    await client.change_presence(status= discord.Status.online,)

@tree.command(name = "teste", description = "Testando o comando", guild=discord.Object(id=874833976085344307)) #Teste
async def teste(interaction):

    await interaction.response.send_message("Salve, eu to online")

@tree.command(name = "equação", description = "Calcular equação do segundo grau", guild=discord.Object(id=874833976085344307)) #Equação do segundo Grau
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
        embed.add_field(name="O valor de delta é:", value=f"{delta}", inline=False)
        embed.add_field(name="O valor da raiz de delta é:", value=f"{raiz}",inline=False)
        embed.add_field(name="O valor de x1:", value=f"{x1}",inline=False)
        embed.add_field(name="O valor de x2:", value=f"{x2}",inline=False)
        await interaction.response.send_message(embed = embed)

@tree.command(name="calcular", description="Cálculos básicos", guild=discord.Object(id=874833976085344307))
async def calcular(interaction, valor: str):
    try:
        resposta = eval(valor)
    except:
        await interaction.response.send_message("Desculpe, a expressão inserida é inválida.")
        return
    await interaction.response.send_message(f"A resposta é: {resposta}")

@tree.command(name="geradorcpf", description="Vai gerar um CPF", guild=discord.Object(id=874833976085344307))
async def geradorcpf(interaction):
    cpf = CPF.generate()
    formatedcpf = CPF.format(cpf)
    await interaction.response.send_message(f"CPF: {formatedcpf}")

@tree.command(name="validadorcpf", description="Valida o CPF informado, informa o cpf sem os . e -", guild=discord.Object(id=874833976085344307))
async def validaorcpf(interaction, cpf: str):
    fcpf = CPF.format(cpf)
    validadorcpf = CPF.validate(fcpf)
    if validadorcpf == True:
        await interaction.response.send_message(f"O CPF: {fcpf} é verdadeiro!")
    elif validadorcpf == False:
        await interaction.response.send_message(f"O CPF: {fcpf} é falso!")
    


client.run(discord_token)
