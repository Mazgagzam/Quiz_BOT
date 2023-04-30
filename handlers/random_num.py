from aiogram import Dispatcher

from aiogram.types import *

from database.db_arg import db

async def random_num(msg: Message):

    global db

    db.new_people(msg)

  

    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))

    await msg.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

