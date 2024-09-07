import logging
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from decouple import config
import os

TOKEN = config('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

admin = [2057932633, ]

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен")

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello!')

@dp.message_handler(commands=['file'])
async def file_handler(message: types.Message):
    folder = 'lesson1.py'

    file_path = os.path.join(folder)

    with open(file_path, 'rb') as file:
        await message.answer_document(file)

@dp.message_handler()
async def squaring_handler(message: types.Message):
    if message.text.isdigit():
        await message.answer(int(message.text)**2)
    else:
        pass


@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
