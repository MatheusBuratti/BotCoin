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
        else:
            listamoedas = cryptocompare.get_coin_list(format=False)
            for item in listamoedas.keys():
                x = listamoedas.get(item)
                nome = x.get("CoinName")
                nome = nome.upper()
                if nome == moeda:
                    return x.get("Name")        
        return moeda
        
    @commands.command(aliases=["coin","preço","preco"])
    async def moeda(self,ctx,*args):
        if args == ():
            await ctx.send("Utilizar junto com nome da moeda. Digite \".help moeda\" para mais informações.")
        else:
            moeda = self.validarMoeda(' '.join(args))
            if moeda is None:
                await ctx.send("Moeda não encontrada.")
            else:
                valores = str(cryptocompare.get_price(moeda, currency=['BRL','USD']))
                valores = valores.translate({ord(i): None for i in ',}{: '})
                valores = valores.split('\'')
                listamoedas = cryptocompare.get_coin_list(format=False)
                moeda = listamoedas.get(moeda)
                embed = Embed(colour=Colour.blurple(),title=moeda.get("CoinName"))
                embed.add_field(name=valores[3],value=valores[4]) # valores[3] == 'BRL'   valores[4] == valor da moeda em BRL
                embed.add_field(name=valores[5],value=valores[6]) # valores[5] == 'USD'   valores[5] == valor da moeda em USD
                await ctx.send(embed=embed)

    @commands.command(aliases=["add"])
    async def adicionar(self,ctx,*args):
        if args == ():
            await ctx.send("Utilizar junto com nome da moeda. Digite \".help adicionar\" para mais informações.")
        else:
            moeda = self.validarMoeda(' '.join(args))
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
                await ctx.send("Adicionada!")

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
            await ctx.send("Removida!")

    @commands.command(aliases=["ls","lista"])
    async def listar(self,ctx):
        file = open("data.txt","r")
        dic = ast.literal_eval(file.read())
        file.close()
        if str(ctx.author) in dic:
            lista = dic.get(str(ctx.author))
            for moeda in lista:
                valores = str(cryptocompare.get_price(moeda, currency=['BRL','USD']))
                valores = valores.translate({ord(i): None for i in ',}{: '})
                valores = valores.split('\'')
                embed = Embed(colour=Colour.blurple(),title=valores[1]) # valores[1] == moeda
                embed.add_field(name=valores[3],value=valores[4]) # valores[3] == 'BRL'   valores[4] == valor da moeda em BRL
                embed.add_field(name=valores[5],value=valores[6]) # valores[5] == 'USD'   valores[5] == valor da moeda em USD
                await ctx.send(embed=embed)
        else:
            await ctx.send("Não encontrado!")


def setup(bot):
    bot.add_cog(Moeda(bot))

