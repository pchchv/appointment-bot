import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    eng_greeting = "Hi " + message.from_user.first_name  # TODO: Write welcoming messages
    ru_greeting = "Привет " + message.from_user.first_name
    if message.from_user.language_code == 'ru':
        await message.reply(ru_greeting)
    else:
        await message.reply(eng_greeting)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    ru_help = ""  # TODO: Write helping messages
    eng_help = ""
    if message.from_user.language_code == 'ru':
        await message.reply(ru_help)
    else:
        await message.reply(eng_help)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
