import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = 'YOUR_BOT_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Рассчитать", "Информация"]
keyboard.add(*buttons)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Выберите действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост в сантиметрах:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer("Введите свой вес в килограммах:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5

    await message.answer(f"Ваша норма калорий: {calories} ккал в день.")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)