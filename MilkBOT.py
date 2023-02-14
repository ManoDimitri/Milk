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
    raiz = sqrt (delta)
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b -raiz) / (2 * a)
    #embed = discord.Embed(title="Equação do segundo grau :",
    #description=b**2 - 4*a*c,color=0x9208ea)
    #embed.set_footer(text="Criado por Dimitri")
    #embed.send(embed=embed)
    await ctx.send("Equação do segundo grau")
    await ctx.reply(f"Equação do segundo grau {os.linesep}O valores é a= {a} b= {b} c= {c} {os.linesep}O valor de delta é: {delta} {os.linesep}O valor da raiz do delta é:{raiz} {os.linesep}O valor de x1: {x1} {os.linesep}O valor de x2: {x2}")
    
    
client.run(discord_token)
