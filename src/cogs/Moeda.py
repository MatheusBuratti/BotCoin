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
        pass

    @commands.command(aliases=["coin","preço","preco"])
    async def moeda(self,ctx,argument):
        pass

def setup(bot):
    bot.add_cog(Moeda(bot))

