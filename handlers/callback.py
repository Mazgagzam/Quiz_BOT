from random import randint

from aiogram import Dispatcher

from aiogram import types

#callback_query_handler(text="random_value")

async def send_random_value(call: types.CallbackQuery):

  await call.message.answer(str(randint(1, 10)))
