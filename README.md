# Discord Bot

This project is a Discord bot that interacts with the GPT-4 Turbo API to provide AI-driven responses in a Discord server.

## Project Structure

```
discord-bot
├── src
│   ├── bot.py        # Main logic for the Discord bot
│   ├── api.py        # Handles communication with the GPT-4 Turbo API
│   └── config.py     # Configuration settings and environment variable management
├── requirements.txt   # Lists project dependencies
├── README.md          # Documentation for the project
└── .env               # Environment variables for sensitive information
```

## Setup Instructions

1. **Clone the repository:**

   ```
   git clone https://github.com/Muhammadkafaby/bot-AI-Discord.git
   cd discord-bot
   ```

2. **Create a virtual environment:**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your Discord bot token and API endpoint:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   API_ENDPOINT=https://api.zpi.my.id/v1/ai/gpt-4-turbo
   ```

   The bot will only respond to messages in channels with IDs that match `TARGET_CHANNEL_ID`. which is located in bot.py

## Usage Guidelines

- Run the bot using the following command:

  ```
  python src/bot.py
  ```

- The bot will listen for messages in the Discord server and respond using the GPT-4 Turbo API.

## Features

- Responds to user messages with AI-generated content.
- Configurable through environment variables for security.
- Easy to set up and extend with additional features.

## Contributing

Feel free to submit issues or pull requests to enhance the functionality of the bot.
