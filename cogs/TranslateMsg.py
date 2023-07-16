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

class TranslateMsg(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.ctx_menu = app_commands.ContextMenu(
            name='Translate Message',
            callback=self.TranslateMsg, # set the callback
        )
        client.tree.add_command(self.ctx_menu) # add the context menu to the tree
        
    async def TranslateMsg(self, interaction: discord.Interaction, text: discord.Message):

        await interaction.response.defer()

        user_id = interaction.user.id
        document = db.UserLangs.find_one({"_id": user_id})

        # check if user has preferred lang setup

        if document is not None:
            lang = document['lang']
        else:
            await interaction.followup.send("You don't have a preferred language set up! To do so, please use `/setlang` first :)", ephemeral=True)
            return

        # actual command

        ohno = "Hey, developer here, don't get me in trouble please lol"
        prompt = f"Translate \"{text.content}\" into {lang} like a native speaker. Don't romanize anything or put it in quotes."

        bad = openai.Moderation.create(input=text.content)

        if not bad.results[0].flagged:
            msg = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=[{"role": "user", "content": prompt}])
            
            response = msg.choices[0].message.content
            donate = "Helpful? Consider using `/donate`"

            # response

            await asyncio.sleep(delay=0)
            await interaction.followup.send(f"{response}\n\n{text.jump_url}")

            # donate message 

            chance = randint(1, 100000)
            if chance > 90000:
                await interaction.followup.send(f"{donate}", ephemeral=True)
        else:
            await asyncio.sleep(delay=0)
            await interaction.followup.send(ohno)

async def setup(client:commands.Bot):
    await client.add_cog(TranslateMsg(client))