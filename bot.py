import discord
import asyncio

TOKEN = ''     # Replace with your bot's token
CHANNEL_ID = 0 # Replace with your channel ID
MESSAGE = 'Hey!'

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    
    if channel:
        await channel.send(MESSAGE)
        print("Message sent successfully.")
        
    else:
        print("Failed to find the channel.")
        
    await client.close()
    
client.run(TOKEN)