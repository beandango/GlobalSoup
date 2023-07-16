import discord
from discord.ext import commands
from discord import app_commands
from pymongo import MongoClient
import os

mongo = MongoClient(os.environ['MONGO_URL'])
db = mongo.Soup

class SetLang(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="setlang", description="set your preferred language")
    async def setlang(self, interaction: discord.Interaction, lang: str):

        user_id = interaction.user.id
        db.UserLangs.update_one({"_id": user_id}, {"$set": {"lang": lang}}, upsert=True)
        
        await interaction.response.send_message(f"Your preferred language has been set to `{lang}`", ephemeral=True)

async def setup(client:commands.Bot):
    await client.add_cog(SetLang(client))




