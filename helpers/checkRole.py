import discord
from discord.ext import commands
from discord import app_commands
import bot

async def check_role_in_guild(guild_id, user_id, role_name):
    # Fetch the Guild and User objects by their ID
    guild = bot.get_guild(guild_id)
    member = guild.get_member(user_id)

    if not member:
        print("Member not found")
        return

    # Check if the role is in the member's roles
    if any(role.name == role_name for role in member.roles):
        return True
    else:
        return False
