from aiogram import types, Dispatcher
from buttons import start
from config import bot

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello!',
                           reply_markup=start)
def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
