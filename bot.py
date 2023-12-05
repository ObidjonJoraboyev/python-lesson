import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6629454001:AAEJhGA5bJAmoupRrDvTJ-0V3LVs9y2VFJI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"{message.from_user.first_name} salom men viki botman obidjon tomonidan yaratildim")
    
    
@dp.message_handler()
async def echo(message: types.Message):
    a=message.text[::-1]
    await message.answer(a)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)