OwO Farm Bot Auto-Hunt
Description
The OwO Farm Bot Auto-Hunt script is designed to automate gameplay for the OwO Discord game. Utilizing discord.py and pyautogui, this Python script interacts with Discord channels, detects specific messages, and performs game actions to simulate a human player. The bot is capable of sending random chat messages, executing various game commands, and taking breaks to maintain a natural interaction pattern.

Features
Discord Bot Integration: Connects to your Discord server and monitors a designated channel for specific messages that trigger the script to stop.
Automated Game Actions: Executes predefined actions in the OwO game such as "OwO hunt," "oh," and "OwO battle" with randomized intervals to mimic human behavior.
Realistic Chat Interaction: Sends a variety of predefined chat messages to simulate user engagement and activity.
Customizable Settings: Easily adjust the bot token, server ID, and channel ID. Customize work durations, break intervals, and other parameters to suit your needs.
Break Management: Automatically takes breaks at randomized intervals to maintain a natural activity pattern and avoid detection.
Graceful Shutdown: Monitors for specific warning messages or links to safely stop the script.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/umeshsingh11/Owo-farm-bot-autohunt.git
cd Owo-farm-bot-autohunt
Install Dependencies:

bash
Copy code
pip install pyautogui discord.py
Configure the Script:

Open owo_auto_hunt.py and replace TOKEN, GUILD_ID, and CHANNEL_ID with your own Discord bot token, server ID, and channel ID.
Run the Script:

bash
Copy code
python owo_auto_hunt.py
Notes
Ensure that your bot has the required permissions in the server to read and send messages in the specified channel.
Be sure to follow Discord's and the OwO game's terms of service to avoid any violations.
Modify the script settings as needed to match your preferences and operational requirements.
