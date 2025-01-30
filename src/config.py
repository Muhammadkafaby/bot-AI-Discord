import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
API_ENDPOINT = "https://api.zpi.my.id/v1/ai/gpt-4-turbo"