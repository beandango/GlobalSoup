import discord
from discord.ext import commands
from discord import app_commands

class Donate(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="donate", description="Support the Dev!")
    async def donate(self, interaction: discord.Interaction):
        embed = discord.Embed(
            color=discord.Color.dark_green(),
            title="Thank you so much for considering supporting the developer!",
            description="Donate via Kofi: https://ko-fi.com/beandango"
        )
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(client:commands.Bot):
    await client.add_cog(Donate(client))