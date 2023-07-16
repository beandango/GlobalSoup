import os
from random import randint
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext import commands
import dateparse
import openai
from Usages import get_and_increment_usage

openai.api_key = os.getenv("OPENAI_API_KEY")

donate = "Helpful? Consider using `/donate`"
ohno = "Hey, developer here, don't get me in trouble please lol"

class ConvertTime(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="converttime", description="Convert a time into a specified timezone")
    async def converttime(self, interaction: discord.Interaction, time: str):

        response = await dateparse.parse_date_time(time)
        if response == "false":
            await interaction.response.send_message(f"I couldn't find a time in that message :sob:", ephemeral=True)
            return
        else:
            response = int(float(response))
            await interaction.response.send_message(f"<t:{response}>")

            # donate message 
            chance = randint(1, 1000)
            if chance > 800:
                await interaction.followup.send(f"{donate}", ephemeral=True)

async def setup(client:commands.Bot):
    await client.add_cog(ConvertTime(client))
