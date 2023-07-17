import os
from random import randint
import dateparser
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext import commands
from dateutil.parser import parse
import pytz
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

donate = "Helpful? Consider using `/donate`"
ohno = "Hey, developer here, don't get me in trouble please lol"

class ConfirmButtonView(discord.ui.View):
    def __init__(self, content):
        super().__init__()
        self.content = content

    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(self.content)

class ConvertTime(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="converttime", description="Convert a time into a specified timezone")
    async def convert(self, interaction: discord.Interaction, time: str, date: str, timezone: str):

        try:
            # Combine date, time and timezone strings
            datetime_str = f'{date}, {time}, {timezone}'
            
            # Parse the string to datetime
            datetime_obj = dateparser.parse(datetime_str)

            if datetime_obj is None:
                raise ValueError("Couldn't parse datetime string")

            # Convert to UTC timezone
            datetime_obj_utc = datetime_obj.astimezone(pytz.UTC)

            # Convert to UNIX timestamp
            unix_timestamp = int(datetime_obj_utc.timestamp())
            
            # Create the preview message with a button for confirmation
            content = f"<t:{unix_timestamp}>"
            view = ConfirmButtonView(content)
            await interaction.response.send_message(content, ephemeral=True, view=view)
        
        except Exception as e:
            await interaction.response.send_message(f"I couldn't parse the provided information. Please try using a more specific date and time format.", ephemeral=True)

        # donate message 
        chance = randint(1, 1000)
        if chance > 800:
            await interaction.followup.send(f"{donate}", ephemeral=True)

async def setup(client:commands.Bot):
    await client.add_cog(ConvertTime(client))

