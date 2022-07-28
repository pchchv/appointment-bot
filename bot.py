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


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    eng_text = "Hi " + message.from_user.first_name  # TODO: Write welcoming messages
    ru_text = "Привет " + message.from_user.first_name
    if message.from_user.language_code == 'ru':
        await message.reply(ru_text)
    else:
        await message.reply(eng_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
