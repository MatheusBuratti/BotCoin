from discord.colour import Colour
from discord.ext import commands
from discord import Embed
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        bot.remove_command('help')

    @commands.command(aliases=["ajuda"])
    async def help(self,ctx,argument=None):
        embed = Embed(colour=Colour.blurple())
        if argument is None:
            embed.title = "Comandos"
            embed.description = ".ajuda\n.moeda\n.adicionar\n.remover\n.listar\n\nUtilizar .ajuda <nomedocomando> para saber mais sobre."
        elif argument in ("help","ajuda"):
            embed.title = "Ajuda"
            embed.description = "Lista os comandos do Bot. Caso receba o nome do comando como argumento, retorna uma descrição do comando"
        elif argument in ("moeda","coin","preco","preço"):
            embed.title = "Moeda"
            embed.description = "Recebe o nome de uma moeda e retorna o valor atualizado em dólares (USD) e em reais (BRL)."
        elif argument in ("adicionar","add"):
            embed.title = "Adicionar"
            embed.description = "Recebe o nome de uma moeda e adiciona ela à sua lista pessoal de favoritos."
        elif argument in ("remover","rm"):
            embed.title = "Remover"
            embed.description = "Recebe o nome de uma moeda e remove ela da sua lista de favoritos."
        elif argument in ("listar","ls","lista"):
            embed.title = "Listar"
            embed.description = "Retorna os valores atualizado de cada moeda da sua lista de favoritos em dólares (USD) e em reais (BRL)."
        else:
           embed.title = "Comando não encontrado!"
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong")

def setup(bot):
    bot.add_cog(Utils(bot))