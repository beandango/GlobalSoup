import discord
from discord.ext import commands
import os
import dotenv

dotenv.load_dotenv()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=discord.Intents().all())

        self.cogslist = ["cogs.Help", "cogs.Convert", "cogs.Translate", "cogs.SetLang", "cogs.TranslateMsg", "cogs.donate", "cogs.ConvertTime"]
    
    async def setup_hook(self):
        for ext in self.cogslist:
            await self.load_extension(ext)

    async def on_ready(self):
        print(f"Bot connected!")
        await self.change_presence(activity=discord.Game(name="with rats"))
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(e)

client = Client()
client.run(os.environ.get('TOKEN'))