import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents, help_command=None)

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.activity.Game(name="Adhan..  /help"))
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
    
@client.tree.command(name="help", description="help of bot")
async def help(interaction: discord.Interaction):
    embed = embed = discord.Embed(title="Help", color=discord.Color.red(), description='this bot does not use "/" commands, to get prayer times use for example: .gmt+3')
    await interaction.response.send_message(embed=embed)

@client.command(name="gmt+3")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/saudi-arabia/108410/riyadh-prayer-times/'
    
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        
        weget = soup.find("div", class_='pt-card-tiles')
        
        if weget:
         dailyprayers = []
         upcomingprayers = None
        
         for i in weget.select('.prayerTiles'):
            name = i.find('span', class_='prayername').gettext(strip=True)
            time = i.find('span', class_='prayertime').get_text(strip=True)
            
            if 'fajr' in i.get('class', []):
                upcomingprayers = f'{name} - {time}'
            else:
                dailyprayers.append(f'{name} - {time}')
                
            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())
            
            for info in dailyprayers:
                embed.add_field(name='Prayers', value=info, inline=False)
                
            embed.add_field(name='Upcoming Prayers', value=upcomingprayers, inline=False)
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error: {response.status_code} ⚠️")
            
        


client.run("YOUR-BOT-TOKEN")