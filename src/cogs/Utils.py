from discord.colour import Colour
from discord.ext import commands
from discord import Embed
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        bot.remove_command('help')

    @commands.command(aliases=["ajuda"])
    async def help(self,ctx):
        embed = Embed(colour=Colour.blurple(),title="Comandos")
        embed.add_field(name=".moeda", value="<Recebe nome de uma moeda e retorna o valor>")
        embed.add_field(name=".help", value="<Descreve os comandos do Bot>")
        
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong")

def setup(bot):
    bot.add_cog(Utils(bot))