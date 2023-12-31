import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents, help_command=None)

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
    embed = embed = discord.Embed(title="Help", color=discord.Color.red(), description='''this bot does not use "/" commands, to get prayer times use for example: ?UTC+3 or ?UTC-3... *PS: if you're in the UTC±0 timezone do: ?UTC0''')
    embed.add_field(name='''Don't know your timezone? Click Here:''', value='https://en.wikipedia.org/wiki/List_of_UTC_offsets#', inline=False)
    await interaction.response.send_message(embed=embed)

@client.command(name="UTC+3")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/saudi-arabia/108410/riyadh-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
            
@client.command(name="UTC+2")
async def time2(ctx):
    url2 = 'https://www.islamicfinder.org/world/egypt/358619/port-said-prayer-times/'
    
    response2 = requests.get(url2)
    
    if response2.status_code == 200:
        soup = BeautifulSoup(response2.text, 'lxml')
        
        weget2 = soup.find("div", class_="pt-card-tiles")
        
        if weget2:
            dailyprayers2 = []
            upcomingprayers2 = None
            
            for i in weget2.select('.prayerTiles'):
                name2 = i.find('span', class_='prayername').get_text(strip=True)
                time2 = i.find('span', class_='prayertime').get_text(strip=True)
                
                if 'Asr' in i.get("class", []):
                    upcomingprayers2 = f"{name2} - {time2}"
                else:
                    dailyprayers2.append(f"{name2} - {time2}")
                    
            embed2 = discord.Embed(title="Prayer Times", color=discord.Color.green())
            
            for info2 in dailyprayers2:
                embed2.add_field(name="Daily Prayers", value=info2, inline=False)
            
            embed2.add_field(name="Upcoming Prayer", value=upcomingprayers2, inline=False)
            
            await ctx.send(embed=embed2)
            
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response2.status_code} ⚠️")
        
@client.command(name="UTC-10")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/united-states/5856195/honolulu-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC-9")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/french-polynesia/42964311/gambier-islands-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
    
@client.command(name="UTC-9:30")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/french-polynesia/42965087/marquesas-islands-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")

@client.command(name="UTC-8")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/french-polynesia/42963985/clipperton-island-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC-7")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/united-states/5780993/salt-lake-city-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC-6")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/belize/3582677/belize-city-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC-5")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/bahamas/3571824/nassau-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC-4")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/argentina/3435910/buenos-aires-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC-3")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/argentina/3435910/buenos-aires-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC-2")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/brazil/40804673/ilha-fernando-de-noronha-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC-1")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/cape-verde/41891287/cabo-verde-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")

@client.command(name="UTC0")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/burkina-faso/2357048/ouagadougou-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+1")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/albania/3183875/tirana-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+3:30")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/iran/40000001/tehran-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="YA ALIIII", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")

@client.command(name="UTC+4")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/armenia/616052/yerevan-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+4:30")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/pakistan/1172451/lahore-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+5")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/pakistan/1172451/lahore-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+5:30")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/sri-lanka/1248991/colombo-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+5:45")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/nepal/1283240/kathmandu-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+6")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/bhutan/1252416/thimphu-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+6:30")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/myanmar-burma/1298824/yangon-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+7")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/cambodia/1821306/phnom-penh-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+8")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/china/1816670/beijing-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+8:45")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/australia/40361834/eucla-motel-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")

@client.command(name="UTC+9")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/east-timor/1645457/dili-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")

@client.command(name="UTC+9:30")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/australia/2173911/broken-hill-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+10")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/australia/2174003/brisbane-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+10:30")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/australia/2147714/sydney-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+11")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/norfolk-island/45238561/territory-of-norfolk-island-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+12")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/fiji/2198148/suva-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+12:45")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/new-zealand/45117744/chatham-islands-county-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+13")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/samoa/4035413/apia-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")
        
@client.command(name="UTC+14")
async def time(ctx):
    url = 'https://www.islamicfinder.org/world/kiribati/44240787/line-islands-prayer-times/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        weget = soup.find("div", class_="pt-card-tiles")

        if weget:
            dailyprayers = []
            upcomingprayers = None

            for i in weget.select('.prayerTiles'):
                name = i.find('span', class_='prayername').get_text(strip=True)
                time = i.find('span', class_='prayertime').get_text(strip=True)

                if 'fajr' in i.get("class", []):
                    upcomingprayers = f"{name} - {time}"
                else:
                    dailyprayers.append(f"{name} - {time}")

            embed = discord.Embed(title="Prayer Times", color=discord.Color.green())

            for info in dailyprayers:
                embed.add_field(name="Daily Prayers", value=info, inline=False)
            
            embed.add_field(name="Upcoming Prayer", value=upcomingprayers, inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No prayer times found")
    else:
        await ctx.send(f"Error {response.status_code} ⚠️")

client.run("YOUR-BOT-TOKEN-HERE")
