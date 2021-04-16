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

    # Recebe uma string com o nome da moeda e retorna a forma para ela ser usada nos comandos da api
    # Ex: recebe bitcoin e retorna BTC
    def validarComando(self, comando:str) -> str:
        if(comando.lower() in ("bitcoin","btc")):
            return "btc"
        elif(comando.lower() in ("dogecoin","doge")):
            return "doge"
        elif(comando.lower() in ("ethereum","eth")):
            return "eth"
        elif(comando.lower() in ("xrp")):
            return "xrp"
        elif(comando.lower() in ("bitcoin cash","bitcoincash","bch","btch")):
            return "bch"
        elif(comando.lower() in ("litecoin","ltc")):
            return "ltc"
        elif(comando.lower() in ("binance coin","binancecoin","bnb")):
            return "bnb"
        elif(comando.lower() in ("ethereum classic","ethereumclassic","etc")):
            return "etc"
        elif(comando.lower() in ("busd")):
            return "busd"
        elif(comando.lower() in ("tron","trx")):
            return "trx"
        return comando
        

    @commands.command(aliases=["coin","preço","preco"])
    async def moeda(self,ctx,argument):
        moeda = self.validarComando(argument)
        await ctx.send(cryptocompare.get_price(moeda, currency=['BRL','USD']))


def setup(bot):
    bot.add_cog(Moeda(bot))

