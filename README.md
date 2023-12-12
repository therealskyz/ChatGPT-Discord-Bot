# ChatGPT Discord Bot

## Introduction

Developed a discord bot that utilizes OpenAI's ChatGPT APIs to generate responses to queries when prompted. The bot uses gpt-3.5-turbo as the model, if you have access to gpt-4, you can update the model under ![](./app/chatgpt_ai/openai.py) to utilize openai's more powerful chatgpt model for better responses and larger token size.

## Architecture

![arch](./images/Lucidchart%20blank%20diagram.png)

## Technologies Used:

- Python
- Discord API
- ChatGPT API

## Quick Start:

### Add Discord Bot to server

    A bot must be added to server first. First create discord app through developer portal which can be found here:
    https://discord.com/developers/applications

    Then subsequently add bot to a server of your choosing by copying and pasting the bot url to server.

### Generate Discord Development Secret Token

    Generated from Discord Developer Portal upon creation of discord application.

### Generate OpenAI ChatGPT Secret Key

    Generated from OpenAI developer platform.

### Load onto ".env" file

    Copy and paste the two api keys into a .env file. These are required so that the discord bot and chatgpt APIs work.

### Run the Bot

    The bot is started by running the following command:

    python3 run.py

    After which the bot should be online and running in the server. It is at this point the bot can be prompted.

### Prompt the Bot

    The bot can be prompted by using the following commands:
    '/ai', '/bot' or '/chatgpt' and then the prompt you would like chatgpt to respond to.

    Example: /ai How are you?
