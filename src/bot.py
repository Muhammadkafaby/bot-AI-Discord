import os
from discord.ext import commands
from discord import Intents
from api import get_gpt_response
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the Discord bot token from the environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

# Define the intents
intents = Intents.default()
intents.message_content = True

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Define the channel ID where the bot should respond
TARGET_CHANNEL_ID = 2136178236xxxxxxx # Ganti dengan ID channel Anda

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id != TARGET_CHANNEL_ID:
        return

    response = get_gpt_response(message.content)
    print(f"API Response: {response}")
    if response and 'data' in response and 'choices' in response['data']:
        content = response['data']['choices']['content']
        if len(content) > 2000:
            content = content[:2000]  # Truncate content to 2000 characters
        await message.channel.send(content)
    else:
        await message.channel.send("Sorry, I couldn't process your request.")

bot.run(TOKEN)
