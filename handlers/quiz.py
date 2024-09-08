from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot

async def quiz_1(message: types.Message):
    quiz_button = InlineKeyboardMarkup()
    button_quiz_1 = InlineKeyboardButton('Дальше...',
                                         callback_data='button_1')
    quiz_button.add(button_quiz_1)

    question = 'BMW or Mercedes?'
    answer = ['BMW', 'Mercedes', 'Lada']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Rus',
        open_period=60,
        reply_markup=quiz_button
    )

async def quiz_2(call: types.CallbackQuery):
    quiz_button = InlineKeyboardMarkup()
    button_quiz_2 = InlineKeyboardButton('Дальше...',
                                         callback_data='button_2')
    quiz_button.add(button_quiz_2)
    question = 'Front ot Back?'
    answer = ['Front', 'Back', 'IOS']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Imposter?',
        open_period=60,
        reply_markup = quiz_button
    )

async def quiz_3(call: types.CallbackQuery):
    question = 'Math or Biology?'
    answer = ['Math', 'Biology', 'PE']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Sports',
        open_period=60,
    )
def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(quiz_3, text='button_2')