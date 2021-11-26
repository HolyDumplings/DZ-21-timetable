from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import pandas as pd

bot = Bot(token="2124043433:AAGV_WqiFhaYbP5VbNUb3vJR7FIBllryd_g")
dp = Dispatcher(bot)

tables = pd.read_html("https://skf-mtusi.ru/rasp/group.php?kurs=itss-zccc&gr=%D0%94%D0%97-21", encoding="UTF-8")
pd.options.display.max_rows = 90
df = (tables[1])
tot = ''


@dp.message_handler(commands=['date'])
async def echo(message: types.Message):
    print(message.text)
    global tot
    try:
        for i in df.itertuples(index=False):
            if '/date ' + i[0] == message.text:
                global tot
                total = " | ".join(i)
                tot += total + '\n'
        await message.answer(tot)
        tot = ''
    except:
        await message.answer('В этот день нет занятий')


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer('Здравстуйте, это бот для расписания группы ДЗ-21')


executor.start_polling(dp, skip_updates=True)
