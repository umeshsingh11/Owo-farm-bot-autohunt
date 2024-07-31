import pyautogui
import time
import threading
import random
import re
import discord
from discord.ext import commands

TOKEN = 'MTA5MjEwNDQ4MTQ4NDgzMjc2OA.G0cP0O.XmfC-oRYh2ao8d_nb8vSZnGbE1LO-2MS8CxFk0'  # Replace with your bot token
GUILD_ID = 1231583214204883036  # Replace with your guild/server ID
CHANNEL_ID = 1233594021482598500  # Replace with your channel ID

# Global flag to stop the script permanently
stop_flag = threading.Event()

# Define the necessary intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Initialize Discord bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event to detect messages
@bot.event
async def on_message(message):
    if message.guild.id == int(GUILD_ID) and message.channel.id == int(CHANNEL_ID):
        if contains_link(message.content):
            print("Link detected in chat! Stopping the script permanently.")
            stop_script()
        elif is_warning_message(message.content):
            print("Warning message detected! Stopping the script permanently.")
            stop_script()

def stop_script():
    print("Stopping the script permanently...")
    stop_flag.set()

def random_sleep(min_time, max_time):
    """Sleep for a random amount of time between min_time and max_time seconds."""
    sleep_time = random.uniform(min_time, max_time)
    time.sleep(sleep_time)

def perform_action(action, interval_range):
    """Perform an action with random intervals."""
    if stop_flag.is_set():
        return
    wait_time = random.uniform(*interval_range)
    print(f"Waiting for {wait_time:.2f} seconds before typing: {action}")
    
    # Countdown
    for i in range(int(wait_time), 0, -1):
        if stop_flag.is_set():
            return
        print(f"{i} seconds remaining...", end='\r')
        time.sleep(1)
    
    pyautogui.write(action)
    pyautogui.press('enter')

def contains_link(message):
    """Check if the message contains a link."""
    url_regex = re.compile(r'(https?://\S+|www\.\S+)')
    return bool(url_regex.search(message))

def is_warning_message(message):
    """Check if the message matches the specific warning pattern."""
    warning_phrases = [
        r'⚠️ \| @\w+, are you a real human\? Please use the link below so I can check!',
        r'Please complete this within 10 minutes or it may result in a ban!',
        r'are you a real human\?',
        r'may result in a ban!',
        r'Please complete this within 10 minutes'
    ]
    for phrase in warning_phrases:
        if re.search(phrase, message):
            return True
    return False

def send_random_chats():
    """Send random chat messages to simulate human interaction."""
    chat_messages = [
        "Hey everyone!", 
        "What's up?", 
        "This game is fun!", 
        "Any tips for a newbie?", 
        "I'm loving this game!",
        "How's everyone doing?",
        "Anyone up for a chat?",
        "I'm new here, any advice?",
        "What's your favorite part of the game?",
        "Having a great time here!",
        "Just started playing, loving it so far!",
        "Can anyone help me with something?",
        "What's the best strategy for this game?",
        "How long have you all been playing?",
        "Any cool tips for a beginner?",
        "I'm learning a lot from you all!",
        "Thanks for the tips, everyone!",
        "This community is awesome!",
        "Just completed a new milestone!",
        "Enjoying every bit of this game!"
    ]
    random.shuffle(chat_messages)
    for message in chat_messages[:random.randint(2, 5)]:
        if stop_flag.is_set():
            return
        if contains_link(message):
            print("Link detected! Stopping the script permanently.")
            stop_script()
            return
        perform_action(message, (1, 2))

def auto_owo():
    work_duration = random.uniform(8 * 60, 10 * 60)  # Random work duration between 8 and 10 minutes
    pray_interval = 5 * 60  # 5 minutes in seconds
    use_interval = random.uniform(15 * 60, 25 * 60)  # Random interval between 15 and 25 minutes
    counter = 0
    last_use_time = time.time()
    hunt_count = 0
    oh_count = 0
    battle_count = 0
    break_count = 0
    small_break_interval = 3 * 60  # 3 minutes in seconds
    min_gap_between_breaks = 60  # Minimum gap of 1 minute between small break and regular break

    try:
        while not stop_flag.is_set():
            start_time = time.time()
            last_small_break_time = start_time

            while time.time() - start_time < work_duration:
                if stop_flag.is_set():
                    break
                perform_action("OwO", (0.5, 1))
                random_sleep(1, 2)  # Random delay between 1 and 2 seconds before OwO hunt
                action_choice = random.choice(["OwO hunt", "oh", "owo h", "owo b"])  # Include "owo b" in the options
                if action_choice == "OwO hunt":
                    hunt_count += 1
                elif action_choice == "oh":
                    oh_count += 1
                perform_action(action_choice, (1.5, 2))
                random_sleep(1, 2)  # Random delay between 1 and 2 seconds before OwO battle
                perform_action("OwO battle", (1.5, 2))
                battle_count += 1
                random_sleep(10, 20)  # Random delay between sets

                counter += 10
                if counter >= pray_interval:
                    perform_action("OwO pray", (1, 1.5))
                    counter = 0

                if time.time() - last_use_time >= use_interval:
                    use_items = ["069", "075", "074", "068", "051", "052"]
                    for item in use_items:
                        perform_action(f"owo use {item}", (0.5, 1))
                    last_use_time = time.time()
                    use_interval = random.uniform(15 * 60, 25 * 60)

                if random.random() < 0.15:  # 15% chance to send random chat
                    send_random_chats()

                # Check for small break
                current_time = time.time()
                if current_time - last_small_break_time >= small_break_interval and \
                        current_time - start_time + min_gap_between_breaks < work_duration:
                    break_duration = random.uniform(20, 40)  # 20 seconds to max of 40 seconds
                    print(f"Taking a small break for {break_duration:.2f} seconds.")
                    time.sleep(break_duration)
                    print("Small break over, resuming work.")
                    last_small_break_time = current_time
                    break_count += 1

            break_duration = random.uniform(2 * 60, 4 * 60)
            print(f"Taking a break for {break_duration / 60:.2f} minutes.")
            time.sleep(break_duration)
            print("Break over, resuming work.")
            send_random_chats()
            work_duration = random.uniform(8 * 60, 10 * 60)
        
        print(f"Total 'OwO hunt' count: {hunt_count}")
        print(f"Total 'oh' count: {oh_count}")
        print(f"Total 'OwO battle' count: {battle_count}")

    except KeyboardInterrupt:
        print("Script stopped by user.")

# Run the Discord bot in a separate thread
threading.Thread(target=bot.run, args=(TOKEN,)).start()
auto_owo()
