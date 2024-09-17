from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import sizes

class FSM_store(StatesGroup):
    product_name = State()
    size = State()
    category = State()
    cost = State()
    photo = State()

size = ['XL','L', 'M']
async def start_fsm_reg(message: types.Message):
    await message.answer('Введите название товара: ')
    await FSM_store.product_name.set()

async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text

    await message.answer('Введите размер: ',reply_markup= sizes)
    await FSM_store.next()

async def load_size(message: types.Message, state: FSMContext):
    if message.text in size:
        async with state.proxy() as data:
            data['size'] = message.text

        await message.answer('Введите категорию: ', reply_markup=types.ReplyKeyboardRemove())
        await FSM_store.next()
    else:
        await message.answer('Нажимайте на кнопки!')
async def load_category(message: types.Message, state: FSMContext):
     async with state.proxy() as data:
        data['category'] = message.text

     await message.answer('Введите цену: ')
     await FSM_store.next()

async def load_cost(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['cost'] = message.text

        await message.answer('Отправьте фото: ')
        await FSM_store.next()
    else:
        await message.answer('Вводите числа!')


async def load_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    async with state.proxy() as data:
        data['photo'] = photo

    await message.answer_photo(photo=photo,
                               caption=f'Верные ли данные?\n'
                                       f'Название: {data["product_name"]}\n'
                                       f'Размер: {data["size"]}\n'
                                       f'Категория: {data["category"]}\n'
                                       f'Цена: {data["cost"]}\n'
                                       f'Фото: {data["photo"]}\n')
    await state.finish()
def register_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(start_fsm_reg, commands=['store'])
    dp.register_message_handler(load_product_name, state=FSM_store.product_name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_cost, state=FSM_store.cost)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])
