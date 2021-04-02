import os
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self,command_prefix):
        super().__init__(command_prefix)
        self.coglist = ["Utils"]

    async def on_ready(self):
        for cog in self.coglist:
            super().load_extension(f'cogs.{cog}')    
        print("Cogs loaded")

        print("Ready")
    

bot = Bot(command_prefix='.')
bot.run('ODI3NTI5MTA5NTg3NDkyODY1.YGcWig.vJNGtrlhgacKDGW4Waf5Wv9lsFo')