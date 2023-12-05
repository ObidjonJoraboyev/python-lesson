import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6629454001:AAEJhGA5bJAmoupRrDvTJ-0V3LVs9y2VFJI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(" men viki botman")
@dp.message_handler()
async def echo(message: types.Message):
    a = message.text
    ls=[]
    check=True
    for x in a:
        ls.append(x)
    for y in range(len(ls)):
        if ls[y] in "1234567890/*-+":
            check=True
        else:
            check=False
            break
            
    if check == False:
        await message.answer(a[::-1])
    else:
        await message.answer(eval(message.text))
        # try:
        #     await message.answer("matematik amal xato kiritilgan")
        #     print("ZeroDivisionError: division by zerro")
        # except ZeroDivisionError:
        #     await message.answer("matematik amal xato kiritilgan")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)