import string
import discord
import requests
import datetime
from discord.ext import tasks, commands

bot = commands.Bot(">")

@bot.event
async def on_ready():
    print("Estou vivo aleluia!")
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    else:
        print(f"Mensagem enviada por: {message.author}")
        print(f"Mensagem enviada em: {message.channel}")
        print(f"Mensagem enviada no servidor: {message.guild}")
        print(f"Conteúdo: {message.content}")    
    if "puta" in  message.content:  
        await message.channel.send(f"Ei! {message.author.name}, não fale desse jeito!")
        await message.delete()
    if "bosta" in message.content:
        await message.channel.send(f"Clbc {message.author.name} seu merdinha você é um bosta msm")
    if "." in message.content:
        await message.channel.send(f"Calei-me perante ao senhor! Meu mestre *{message.author.name}*")


    await bot.process_commands(message)



@bot.command(name="calcular")
async def calculate(ctx, *expression):
    expression = ''.join(expression)
    resposta = eval(expression)
    
    print(f"Foi efetuado um calculo: {ctx.author}")
    print(f"Calculo resultado: {resposta}, calculo: {expression}")

    await ctx.send("**O resultado da operação é: **"+ str(resposta))

@bot.command(name="horario")
async def horario(ctx):
    horas = datetime.datetime.now()
    hora = horas.strftime("%d/%m/%Y às %H:%M:%S")
    await ctx.send(f"Hoje é: {hora}")

@bot.command(name="converter")
async def binance(ctx, coin, base):
    sapi = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")


    data = sapi.json()
    price = data.get("price")

    if price:
        await ctx.send(f"**A moeda {coin} convertida para {base} é equivalente a: {price}**")
    else:
        await ctx.send(f"*A moeda inserida é invalida.*")
    await ctx.send(f"**Estou usando a API da corretora Binance para checar os resultados.**")
    await ctx.send(f"**Para checar as moedas passivas de transmissão use: **>bolsa**")

@bot.command(name="bolsa")
async def bolsinha(ctx): 
    
        br = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL")
        br2 = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=ETHBRL")
        br3 = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=AXSBRL")
        br4 = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=SHIBBRL")
        br5 = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=SOLBRL")
        br7 = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=DOTBRL")

        data = br.json()
        data1 = br2.json()
        data2 = br3.json()
        data3 = br4.json()
        data4 = br5.json()
        data5 = br7.json()
        price = data.get("price")
        price1 = data1.get("price")
        price2 = data2.get("price")
        price3 = data3.get("price")
        price4 = data4.get("price")
        price5 = data5.get("price")

        await ctx.send("*Conversões para a moeda BRL(REAL)*")
        await ctx.send(f"**BITCOIN = BTC:** {price}   **ETHERIUM = ETH:** {price1}")
        await ctx.send(f"**AXIE = AXS:** {price2}   **SHIBA INU = SHIB:** {price3}")
        await ctx.send(f"**SOLANA = SOL:** {price4}   **POLKADOT = DOT:** {price5}")


    

@bot.command(name="stop")
async def stop(ctx):
   await ctx.send(f"**{ctx.author.name}** Não tem permissão pra usar esse comando seu **BOSTA**")       

bot.run("token")