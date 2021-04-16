import os
from discord.ext import commands
from configparser import ConfigParser

class Bot(commands.Bot):
    def __init__(self,command_prefix):
        super().__init__(command_prefix)
        self.coglist = ["Utils","Moeda"]

    async def on_ready(self):
        for cog in self.coglist:
            super().load_extension(f'cogs.{cog}')    
        print("Cogs loaded")

        print("Ready")
    
config = ConfigParser()
config.read("config.ini")
token = config.get("BOT","TOKEN")
bot = Bot(command_prefix='.')
bot.run(token)
