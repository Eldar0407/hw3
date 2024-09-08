from aiogram import types, Dispatcher
from config import bot
import random

games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
async def echo_handler(message: types.Message):
    random_game = random.choice(games)

    if message.text == "/game":
        await message.answer_dice()
    elif message.text == '/random_game':
        await bot.send_dice(chat_id=message.from_user.id, emoji=random_game)
    elif message.text == '/game2':
        await message.answer("Игрок бросил кость:")
        player_dice = await message.answer_dice()
        await message.answer("Бот бросил кость:")
        bot_dice = await message.answer_dice()
        if player_dice.dice.value > bot_dice.dice.value:
            await message.answer("Ты победил!")
        elif player_dice.dice.value < bot_dice.dice.value:
            await message.answer("Бот победил!")
        else:
            await message.answer("Ничья!")
    else:
        await message.answer(message.text)
def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)