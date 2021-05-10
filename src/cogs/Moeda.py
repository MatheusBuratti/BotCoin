import ast
from discord.colour import Colour
from discord.ext import commands
from discord import Embed
from configparser import ConfigParser
import cryptocompare

class Moeda(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        config = ConfigParser()
        config.read("config.ini")
        self.token = config.get("CRYPTOCOMPARE","TOKEN")

    # Recebe uma string com o nome da moeda e retorna a forma para ela ser usada nos comandos da api,
    # caso ela não exista na lista da api, retorna None.
    # Ex: recebe bitcoin e retorna BTC
    def validarMoeda(self, moeda:str) -> str:
        moeda = moeda.upper()
        if moeda in ("BITCOIN","BTC"):
            return "BTC"
        elif moeda in ("DOGECOIN","DOGE"):
            return "DOGE"
        elif moeda in ("ETHEREUM","ETH"):
            return "ETH"
        elif moeda in ("XRP"):
            return "XRP"
        elif moeda in ("BITCOIN CASH","BITCOINCASH","BCH","BTCH"):
            return "BCH"
        elif moeda in ("LITECOIN","LTC"):
            return "LTC"
        elif moeda in ("BINANCE COIN","BINANCECOIN","BNB"):
            return "BNB"
        elif moeda in ("ETHEREUM CLASSIC","ETHEREUMCLASSIC","ETC"):
            return "ETC"
        elif moeda in ("BUSD"):
            return "BUSD"
        elif moeda in ("TRON","TRX"):
            return "TRX"
        elif moeda not in cryptocompare.get_coin_list(format=True):
            return None
        return moeda
        

    @commands.command(aliases=["coin","preço","preco"])
    async def moeda(self,ctx,argument):
        moeda = self.validarMoeda(argument)
        if moeda is None:
            await ctx.send("Moeda não encontrada, tente usar a forma abreviada.")
        else:
            await ctx.send(cryptocompare.get_price(moeda, currency=['BRL','USD']))

    @commands.command(aliases=["add"])
    async def adicionar(self,ctx,argument):
        moeda = self.validarMoeda(argument)
        if moeda is None:
            await ctx.send("Moeda não encontrada, tente usar a forma abreviada.")
        else:
            file = open("data.txt","r")
            dic = ast.literal_eval(file.read())
            file.close()
            if str(ctx.author) in dic:
                lista = dic.get(str(ctx.author)) 
                if moeda not in lista:
                    lista.append(str(moeda))
            else:
                lista = list()
                lista.append(str(moeda))
                dic[str(ctx.author)] = lista

            file = open("data.txt","w")
            file.write(str(dic))
            file.close()

    @commands.command(aliases=["rm"])
    async def remover(self,ctx,argument):
        moeda = self.validarMoeda(argument)
        if moeda is None:
            await ctx.send("Moeda não encontrada, tente usar a forma abreviada.")
        else:
            file = open("data.txt","r")
            dic = ast.literal_eval(file.read())
            file.close()
            if str(ctx.author) in dic:
                lista = dic.get(str(ctx.author))
                if moeda in lista:
                    lista.remove(str(moeda))
                if len(lista) == 0:
                    dic.pop(str(ctx.author))
            file = open("data.txt","w")
            file.write(str(dic))
            file.close()

    @commands.command(aliases=["l","lista"])
    async def listar(self,ctx):
        file = open("data.txt","r")
        dic = ast.literal_eval(file.read())
        file.close()
        if str(ctx.author) in dic:
            lista = dic.get(str(ctx.author))
            for item in lista:
                await ctx.send(cryptocompare.get_price(item, currency=['BRL','USD']))


def setup(bot):
    bot.add_cog(Moeda(bot))

