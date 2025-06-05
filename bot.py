import discord
import asyncio
import os
import subprocess

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
    cmd = message.content
    
    if message.author == client.user:
        return
    
    result = subprocess.run(['type', 'C:\\Users\\marti\\Desktop\\Important Info.txt'], capture_output=True, text=True, shell=True)
    output = result.stdout.strip()    
    
    for i in range(0, len(output), 1990):
        
        if i == 0:
            await message.channel.send(f"{cmd}:")

        chunk = output[i:i+1990]
        await message.channel.send(f"```{chunk}```")
    
client.run(TOKEN)