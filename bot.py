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
    print(f'Message was: {message.content}')
    
client.run(TOKEN)