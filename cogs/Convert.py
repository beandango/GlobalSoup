from random import randint
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext import commands
import dateparse

donate = "Helpful? Consider using `/donate`"
ohno = "Hey, developer here, don't get me in trouble please lol"

class Convert(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.ctx_menu = app_commands.ContextMenu(
            name='Convert Time',
            callback=self.convert, # set the callback
        )
        client.tree.add_command(self.ctx_menu) # add the context menu to the tree
        
    async def convert(self, interaction: discord.Interaction, message: discord.Message):

        response = await dateparse.parse_date_time(message.content)
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
    await client.add_cog(Convert(client))

