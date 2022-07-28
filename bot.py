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


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    eng_text = "Hi " + message.from_user.first_name  # TODO: Write welcoming messages
    ru_text = "Привет " + message.from_user.first_name
    await message.reply(eng_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)