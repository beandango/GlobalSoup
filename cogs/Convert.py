import discord
from discord.ext import commands
from discord import app_commands
from discord.ext import commands
import re
from dateutil.parser import parse
from timezoneDict import timezones
from tzinfos import tzinfos

class Convert(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.ctx_menu = app_commands.ContextMenu(
            name='Convert Time',
            callback=self.convert, # set the callback
        )
        client.tree.add_command(self.ctx_menu) # add the context menu to the tree
        
    async def convert(self, interaction: discord.Interaction, message: discord.Message):

        pattern = re.compile(r'\b((1[0-2]|0?[1-9]):([0-5][0-9])?(am|pm|AM|PM))\b|\b(([01]?[0-9]|2[0-3]):[0-5][0-9])\b')

        # Find a time and timezone in the message
        matches = pattern.findall(message.content)
        timezone_matches = [tz for tz in timezones if tz in message.content.upper()]

        if matches and timezone_matches:
            # If a time and timezone were found, convert the time to Unix timestamp
            time_string = matches[0][0] if matches[0][0] else matches[0][4]
            time_with_tz = time_string + ' ' + timezone_matches[0]
            dt = parse(time_with_tz, tzinfos=tzinfos)  # parse the time string to a datetime object
            timestamp = int(dt.timestamp())  # convert the datetime object to Unix timestamp

            await interaction.response.send_message(f"<t:{timestamp}> \n<t:{timestamp}:R>\n\n{message.author}\n{message.jump_url}")

        else:
            await interaction.response.send_message(f"Could not find a time to convert :( | {message.jump_url}",ephemeral=True)

async def setup(client:commands.Bot):
    await client.add_cog(Convert(client))

