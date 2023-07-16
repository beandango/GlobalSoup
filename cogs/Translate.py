import asyncio
from random import randint
import re
import discord
from discord.ext import commands
from discord import app_commands
import os
import openai
from pymongo import MongoClient

openai.api_key = os.getenv("OPENAI_API_KEY")

mongo = MongoClient(os.environ['MONGO_URL'])
db = mongo.Soup

class Translate(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="translate", description="Translate text into any language!")
    async def Translate(self, interaction: discord.Interaction, text: str, lang: str):

        await interaction.response.defer()

        ohno = "Hey, developer here, don't get me in trouble please lol"
        prompt = f"Translate \"{text}\" into {lang} like a native speaker. Don't romanize anything or put it in quotes."

        bad = openai.Moderation.create(input=text)

        if not bad.results[0].flagged:
            msg = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=[{"role": "user", "content": prompt}])
            
            response = msg.choices[0].message.content
            donate = "Helpful? Consider using `/donate`"

            # response

            await asyncio.sleep(delay=0)
            await interaction.followup.send(f"{response}")

            # donate message 
            
            chance = randint(1, 100000)
            if chance > 90000:
                await interaction.followup.send(f"{donate}", ephemeral=True)
        else:
            await asyncio.sleep(delay=0)
            await interaction.followup.send(ohno)

async def setup(client:commands.Bot):
    await client.add_cog(Translate(client))