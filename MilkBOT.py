import discord
from discord.ext import commands
from math import sqrt
from dotenv import load_dotenv
import os

discord_token = os.getenv('TOKEN')

client = commands.Bot(command_prefix= "$", help_command=None, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Eu entrei como {client.user.name}")

    await client.change_presence(status= discord.Status.online,)

@client.command()
async def teste(ctx):

    await ctx.reply(f"Salve, eu to online {ctx.author}")

@client.command()
async def equação(ctx, a: int, b: int, c: int):
    delta = b**2 - 4*a*c
    if a == 0:
        await ctx.reply("Se a = 0, não é uma equação do segundo grau. Execute o comando novamente em que o valor de A seja diferente de 0.")
    elif delta < 0:
        await ctx.reply(f"O valor de delta é menor que 0, a equação não apresentará raízes. Valor de delta: {delta}")
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
        await ctx.send(embed = embed)
        
client.run(discord_token)
