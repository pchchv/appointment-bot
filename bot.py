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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.from_user.language_code == 'ru':
        buttons = ['Запись', 'Мои записи', 'Регистрация', 'Вход']
        greeting = 'Привет ' + message.from_user.first_name  # TODO: Write welcoming message
    else:
        buttons = ['Appointment', 'My appointments', 'Sign up', 'Sign in']
        greeting = 'Hi ' + message.from_user.first_name      # TODO: Write welcoming message
    keyboard.add(*buttons)
    await message.reply(greeting, reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    if message.from_user.language_code == 'ru':
        help_message = ''  # TODO: Write helping message
    else:
        help_message = ''  # TODO: Write helping message
    await message.reply(help_message)


@dp.message_handler(text=['Sign up', 'Регистрация'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends the "Sign up" message or clicks the "Sign up" button.
    """
    if message.from_user.language_code == 'ru':
        appointment_message = ''  # TODO: Write message
    else:
        appointment_message = ''  # TODO: Write message
    # TODO: Implement a sign up function
    await message.reply(appointment_message)


@dp.message_handler(text=['Sign in', 'Вход'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends the "Sign in" message or clicks the "Sign in" button.
    """
    if message.from_user.language_code == 'ru':
        appointment_message = ''  # TODO: Write message
    else:
        appointment_message = ''  # TODO: Write message
    # TODO: Implement a sign in function
    await message.reply(appointment_message)


@dp.message_handler(text=['Appointment', 'Запись'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends the "Appointment" message or clicks the "Appointment" button.
    """
    if message.from_user.language_code == 'ru':
        appointment_message = ''  # TODO: Write message
    else:
        appointment_message = ''  # TODO: Write message
    # TODO: Implement the appointment function
    await message.reply(appointment_message)


@dp.message_handler(text=['My appointments', 'Мои записи'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends the "My appointments" message
    or clicks the "My appointments" button.
    """
    if message.from_user.language_code == 'ru':
        appointment_message = ''  # TODO: Write message
    else:
        appointment_message = ''  # TODO: Write message
    # TODO: Implement a function to view user appointments
    await message.reply(appointment_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
