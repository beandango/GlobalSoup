import discord
from discord.ext import commands
from discord import app_commands

class Timezones(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="timezones", description="See all timezones that the bot currently recognized")
    async def timezones(self, interaction: discord.Interaction):
        embed = discord.Embed(
            color=discord.Color.dark_green(),
            title="Help",
            description="\n'EST': 'US/Eastern',          # Eastern Standard Time" \
                        "\n'EDT': 'US/Eastern',          # Eastern Daylight Time" \
                        "\n'PST': 'US/Pacific',          # Pacific Standard Time" \
                        "\n'PDT': 'US/Pacific',          # Pacific Daylight Time" \
                        "\n'CST': 'US/Central',          # Central Standard Time" \
                        "\n'CDT': 'US/Central',          # Central Daylight Time" \
                        "\n'MST': 'US/Mountain',         # Mountain Standard Time" \
                        "\n'MDT': 'US/Mountain',         # Mountain Daylight Time" \
                        "\n'EEST': 'Europe/Helsinki',    # Eastern European Summer Time" \
                        "\n'EET': 'Europe/Helsinki',     # Eastern European Time" \
                        "\n'UTC': 'UTC',                 # Coordinated Universal Time" \
                        "\n'GMT': 'Etc/GMT',             # Greenwich Mean Time" \
                        "\n'BST': 'Europe/London',       # British Summer Time" \
                        "\n'IST': 'Europe/Dublin',       # Irish Standard Time" \
                        "\n'CEST': 'Europe/Paris',       # Central European Summer Time" \
                        "\n'CET': 'Europe/Paris',        # Central European Time" \
                        "\n'WET': 'Europe/Lisbon',       # Western European Time" \
                        "\n'WEST': 'Europe/Lisbon',      # Western European Summer Time" \
                        "\n'AEST': 'Australia/Sydney',   # Australian Eastern Standard Time" \
                        "\n'AEDT': 'Australia/Sydney',   # Australian Eastern Daylight Time" \
                        "\n'ACST': 'Australia/Adelaide', # Australian Central Standard Time" \
                        "\n'ACDT': 'Australia/Adelaide', # Australian Central Daylight Time" \
                        "\n'AWST': 'Australia/Perth',    # Australian Western Standard Time" \
                        "\n'NZST': 'Pacific/Auckland',   # New Zealand Standard Time" \
                        "\n'NZDT': 'Pacific/Auckland',   # New Zealand Daylight Time" \
                        "\n'HST': 'Pacific/Honolulu',    # Hawaii Standard Time" \
                        "\n'HDT': 'Pacific/Honolulu',    # Hawaii Daylight Time" \
                        "\n'AKST': 'US/Alaska',          # Alaska Standard Time" \
                        "\n'AKDT': 'US/Alaska',          # Alaska Daylight Time" \
                        "\n'AST': 'America/Halifax',     # Atlantic Standard Time" \
                        "\n'ADT': 'America/Halifax',     # Atlantic Daylight Time" \
                        "\n'SAST': 'Africa/Johannesburg',# South Africa Standard Time" \
                        "\n'WAST': 'Africa/Lagos',       # West Africa Standard Time" \
                        "\n'EAT': 'Africa/Nairobi',      # East Africa Time" \
                        "\n'CAT': 'Africa/Maputo',       # Central Africa Time" \
                        "\n'IST': 'Asia/Kolkata',        # Indian Standard Time" \
                        "\n'CST': 'Asia/Shanghai',       # China Standard Time" \
                        "\n'JST': 'Asia/Tokyo',          # Japan Standard Time" \
                        "\n'KST': 'Asia/Seoul',          # Korea Standard Time" \
                        "\n'PHT': 'Asia/Manila',         # Philippine Time" \
                        "\n'MYT': 'Asia/Kuala_Lumpur',   # Malaysia Time" \
                        "\n'SGT': 'Asia/Singapore',      # Singapore Time" \
                        "\n'ICT': 'Asia/Bangkok',        # Indochina Time" \
                        "\n'WIB': 'Asia/Jakarta',        # Western Indonesian Time" \
                        "\n'WITA': 'Asia/Makassar',      # Central Indonesian Time" \
                        "\n'WIT': 'Asia/Jayapura',       # Eastern Indonesian Time" \
                        "\n'IST': 'Asia/Jerusalem',      # Israel Standard Time" \
                        "\n'IDT': 'Asia/Jerusalem',      # Israel Daylight Time" \
                        "\n'IRST': 'Asia/Tehran',        # Iran Standard Time" \
                        "\n'IRDT': 'Asia/Tehran',        # Iran Daylight Time" \
                        "\n'GST': 'Asia/Dubai',          # Gulf Standard Time" \
                        "\n'MSK': 'Europe/Moscow',       # Moscow Standard Time" \
                        "\n'MSD': 'Europe/Moscow',       # Moscow Daylight Time" \
                        "\n'SAMT': 'Europe/Samara',      # Samara Time" \
                        "\n'YEKT': 'Asia/Yekaterinburg', # Yekaterinburg Time" \
                        "\n'OMST': 'Asia/Omsk',          # Omsk Standard Time" \
                        "\n'KRAT': 'Asia/Krasnoyarsk',   # Krasnoyarsk Time" \
                        "\n'IRKT': 'Asia/Irkutsk',       # Irkutsk Time" \
                        "\n'YAKT': 'Asia/Yakutsk',       # Yakutsk Time" \
                        "\n'VLAT': 'Asia/Vladivostok',   # Vladivostok Time" \
                        "\n'MAGT': 'Asia/Magadan',       # Magadan Time" \
                        "\n'PETT': 'Asia/Kamchatka',     # Kamchatka Time" \
                        "\n'AMT' : 'Asia/Yerevan'        # Armenia Time")
        await interaction.response.send_message(embed=embed)

async def setup(client:commands.Bot):
    await client.add_cog(Timezones(client))