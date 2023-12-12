import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from app.chatgpt_ai.openai import chatgpt_response


load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_SECRET')

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command, user_message = None, None

    for text in ['/ai', '/bot', '/chatgpt']:
        if message.content.startswith(text):
            command = message.content.split(' ')[0]
            user_message = message.content.replace(text, '')
            print(command, user_message)

    if command == '/ai' or command == '/bot' or command == '/chatgpt':
        bot_response = chatgpt_response(prompt=user_message)
        await message.channel.send(f"Answer: {bot_response}")
