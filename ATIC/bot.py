import discord
import asyncio
from datetime import datetime, timedelta
import responses
from tic_tac_toe import TicTacToeGame

# Create an Intents object with desired permissions
intents = discord.Intents.default()
intents.messages = True  # For handling messages
intents.dm_messages = True  # If you want to handle direct messages

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    # Prevent bot from responding to its own messages
    if message.author == client.user:
        return

    user_message = str(message.content)
    author_id = message.author.id  # Extract the author's ID

    # Check if the message is empty
    if not user_message:
        return

    user_message = user_message[23:]
    print(user_message)


    # Handle Tic Tac Toe commands
    if user_message.startswith('start tictactoe') or user_message.startswith(' start tictactoe'):
        response = responses.start_tic_tac_toe(message.channel.id)
        await message.channel.send(response)
        return

    if user_message.startswith('move') or user_message.startswith(' move'):
        try:
            position = int(user_message.split()[1])  # Assumes the format is "move <position>"
            author_id = message.author.id  # ID of the player making the move
            response = responses.make_move(message.channel.id, position, author_id)
        except ValueError:
            response = "Please specify a valid position (0-8)."
        await message.channel.send(response)
        return

    elif user_message.startswith('end tictactoe'):
        response = responses.end_tic_tac_toe(message.channel.id)
        await message.channel.send(response)
        return

    # Handle other commands and responses
    response = responses.handle_response(user_message, author_id)
    await message.channel.send(response)

async def reminder_task(client):
    while not client.is_closed():
        current_time = datetime.now()
        # Add your reminder code here
        await asyncio.sleep(60)  # Sleeps for 60 seconds

def run_discord_bot():
    Token = 'MTE3NTg3NjIxMzgwNjQ2OTIxMA.G6mzws.7CeXd3VsBhBkL1NZLi5CPcK8Iy1EpjKcm3s8yA'
    client.run(Token)

if __name__ == '__main__':
    run_discord_bot()
