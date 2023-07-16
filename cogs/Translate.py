import asyncio
from random import randint
import discord
from discord.ext import commands
from discord import app_commands
import os
import openai
from pymongo import MongoClient
from Usages import get_and_increment_usage

openai.api_key = os.getenv("OPENAI_API_KEY")

donate = "Helpful? Consider using `/donate`"
ohno = "Hey, developer here, don't get me in trouble please lol"

mongo = MongoClient(os.environ['MONGO_URL'])
db = mongo.Soup

class Translate(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="translate", description="Translate text into any language!")
    async def Translate(self, interaction: discord.Interaction, text: str, lang: str):

        await interaction.response.defer()

        ohno = "Hey, developer here, don't get me in trouble please lol"
        prompt = f"Translate \"{text}\" into {lang} like a native speaker. Don't romanize anything or put it in quotes, and dont explain it! Just translate it exactly as it is."

        bad = openai.Moderation.create(input=text)

        if not bad.results[0].flagged:
            msg = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=[{"role": "user", "content": prompt}])
            
            response = msg.choices[0].message.content

            # response

            await asyncio.sleep(delay=0)
            await interaction.followup.send(f"{response}")

            user_id = interaction.user.id
            count = await get_and_increment_usage(user_id)

            # donate message 
            chance = randint(1, 10)
            if chance > 5 and count > 10:
                await interaction.followup.send(f"{donate}", ephemeral=True)
        else:
            await asyncio.sleep(delay=0)
            await interaction.followup.send(ohno)

async def setup(client:commands.Bot):
    await client.add_cog(Translate(client))