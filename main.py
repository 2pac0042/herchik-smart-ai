import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Загружаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("✅ Herchik Smart AI запущен!")

# Ответ на любые сообщения
@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.reply("Вы написали: " + message.text)

if name == "__main__":
    executor.start_polling(dp)
