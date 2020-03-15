# Weather Discord Bot
# Arthur Xu
# March 15th, 2020
# Discord Bot that can get the weather. First stab at APIs.

import discord
import random
from discord.ext import commands
import requests

# API address, space for city
api_address = "http://api.openweathermap.org/data/2.5/weather?q="
api_address2 = "&appid='API key here'&units=metric"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Ignores itself
    if message.author == client.user:
        return
    
    # When bot is called
    if message.content.startswith('!weather'):
        msg = message.content
        #Gets the city name (Ignores !weather)
        city = msg[9:]
        # Gets the weather stats
        weatherStats = getStats(city)
        # Outputs the weather stats to the channel
        await message.channel.send("City: "+city+"\n Weather type: "+weatherStats[0]+"\n Temperature: "+weatherStats[1]+"°C\n Wind Speed: "+weatherStats[2]+" KM/H")

def getStats(city):
    # Get weather descriptions
    url = api_address+city+api_address2
    json_data = requests.get(url).json()
    description = str(json_data['weather'][0]["main"])
    temp = str(json_data['main']['temp'])
    windSpeed = str(json_data['wind']['speed'])
    weatherStats = [description, temp, windSpeed]
    return weatherStats

# Bot Token
client.run('Bot Token Here')
