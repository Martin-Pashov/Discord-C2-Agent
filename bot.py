import discord
import asyncio

TOKEN = ''     # Replace with your bot's token
CHANNEL_ID = 1379950289569976330 # Replace with your channel ID
MESSAGE = 'Hey!'

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.channel.id == CHANNEL_ID:
        await message.channel.send(message.content)
    
client.run(TOKEN)