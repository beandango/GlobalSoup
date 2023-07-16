import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="help", description="how does this work ahhhhhhhh")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            color=discord.Color.dark_green(),
            title="Commands",
            description="**/now**\ninput your timezone in all caps, and the bot returns info about your current time in this format: `<t:timestamp>`\n\n**Convert Time**\nif a message contains a time and a recognized timezone code, you can right click on the message -> Apps -> Convert Time, and the bot will display that time in the `<t:timestamp>` format\n\n**/Timezones**\nSee a full list of the currently recognized timezones\n\n**/Translate**\nInput any text and a language to get a translation of that text into that language\n\n**Translate Message**\nFirst use `/setlang` to set your preferred language, then you can right-click on any message, apps->Translate Message, and Soup will translate that message into your preferred language\n\n**/setlang**\nSets your preferred langauge to be used when using the Translate Message command above\n\n**/donate**\nThis bot uses openai's API for translation, which means it isn't free. If you like the bot, consider supporting development using this command!")
        
        await interaction.response.send_message(embed=embed)

async def setup(client:commands.Bot):
    await client.add_cog(Help(client))