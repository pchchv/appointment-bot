import logging
from aiogram import Bot, Dispatcher, types, executor

with open("token.txt", 'r') as t:
    BOT_TOKEN = t.read()
t.close()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
