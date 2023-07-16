from datetime import datetime
import discord
from discord.ext import commands
from discord import app_commands
import re
from dateutil.parser import parse
import pytz
from timezoneDict import timezones
from tzinfos import tzinfos

class Now(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="now", description="Get the current time in a specific timezone")
    async def now(self, interaction: discord.Interaction, timezone: str):
        # Check if the provided timezone is valid
        if timezone not in timezones:
            await interaction.response.send_message(f'`{timezone}` is not a valid timezone. Please provide a valid timezone.',ephemeral=True)
            return

        tz = pytz.timezone(timezones[timezone])
        current_time = datetime.now(tz)
        timestr = current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        dt = parse(timestr, tzinfos=tzinfos)  # parse the time string to a datetime object
        timestamp = int(dt.timestamp())  # convert the datetime object to Unix timestamp

        # Send the current time
        await interaction.response.send_message(f"{timezone}\n{timestr}\n<t:{timestamp}>")

async def setup(client:commands.Bot):
    await client.add_cog(Now(client))



