from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# ===============================================================

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

sizes = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=3).add(
    KeyboardButton(text='XL'),
    KeyboardButton(text='L'),
    KeyboardButton(text='M')
)



quiz_buttons = KeyboardButton('/quiz')
game_buttons = KeyboardButton('/game')
game2_buttons = KeyboardButton('/game2')
random_game_buttons = KeyboardButton('/random_game')


cancel_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))

submit_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                    row_width=2).add(KeyboardButton('Да'), KeyboardButton('Нет'))


start.add(quiz_buttons,game_buttons, game2_buttons,
          random_game_buttons)



# =================================
# ==============================

start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
KeyboardButton('/start')
)

# ===============================================================

start_test_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    )

start_test_1.add(
    KeyboardButton('/start'),
    KeyboardButton('/mem'),
    KeyboardButton('/mem_all'),
    KeyboardButton('/music')
)

# ===============================================================
