import discord
import asyncio
from dotenv import load_dotenv
import os
import subprocess
from io import StringIO


load_dotenv()

MAX_MESSAGE_LENGTH = 1900
MAX_OUTPUT_SIZE = 19000
ALLOWED_USER_IDS = {723426354468487188, 290500457573384202, 598421234316738562} # Replace with your Discord user ID(s)
CHANNEL_ID = 1379950289569976330 # Replace with your channel ID
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if not TOKEN:
    raise ValueError("X Token not found. Please set DISCORD_BOT_TOKEN in your .env file.")


intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

current_directory = os.getcwd()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    
@client.event
async def on_message(message):
    global current_directory
    
    if message.author.bot:
        return

    if message.author.id not in ALLOWED_USER_IDS:
        return

    command = message.content.strip()
    if not command:
        await message.channel.send('Not a valid command!')
        return

        
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
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=current_directory, timeout=10)
        output = (result.stdout + result.stderr).strip()
        
        if not output:
            output = "(No output)"

        if len(output) > MAX_OUTPUT_SIZE:
            output_file = StringIO(output)
            output_file.seek(0)
            discord_file = discord.File(fp=output_file, filename="output.txt")
            await message.channel.send("Output too long, sending as file:", file=discord_file)
        
        else:
            for i in range(0, len(output), MAX_MESSAGE_LENGTH):
                chunk = output[i:i + MAX_MESSAGE_LENGTH]
                await message.channel.send(f"```{chunk}```")

    except subprocess.TimeoutExpired:
        await message.channel.send("Command timed out.")

    except Exception as e:
        await message.channel.send(f"❌ Execution error: {str(e)}")

client.run(TOKEN)