import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def multiply(ctx, left: int, right: int):
    await ctx.send(left * right)   

@bot.command()
async def subtract(ctx, left: int, right: int):
    await ctx.send(left - right) 

@bot.command()
async def divide(ctx, left = 0.0, right = 1):
    await ctx.send(left / right) 

yazitura1=["Yazı","Tura"]
puan=0
@bot.command()
async def yazitura(ctx, cevap):
        a=random.choice(yazitura1)
        cevap = cevap[0].upper()
        if cevap == a:
             puan =+ 1
             await ctx.send(f"{a} doğru tahmin! +1 puan. {puan}")
        else: 
             await ctx.send("Maalesef doğru tahmin edemedin!")     
bot.run("ur token")
