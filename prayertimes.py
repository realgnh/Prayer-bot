import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents, help_command=None)

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.activity.Game(name="Adhan.."))
    print(f"{client.user.name} is ONLINE")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name="ping", description="ping of bot")
async def ping(interaction: discord.Interaction):
    bot_ping = round(client.latency*1000)
    await interaction.response.send_message(f"pong!... {bot_ping}ms")

@client.tree.command(name="prayers")
async def prayertimes(interaction: discord.Interaction):
    embed = discord.Embed(
        color=0xdb0707,
        title='Prayer Times (gmt+3)',
        description='''Fajr: 5:09

                       Duhr: 11:51

                       Asr: 02:50 

                      Magrhib: 05:09 

                       Isha: 06:39'''
    )
    embed.add_field(name="link to countdown of prayer time + daily updated prayer time", value= 'https://www.islamicfinder.org/world')
    await interaction.response.send_message(embed=embed)



client.run("BOT_TOKEN_HERE")
