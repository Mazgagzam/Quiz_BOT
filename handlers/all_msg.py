from aiogram.types import Message

from database.db_arg import db

async def all_msg(msg: Message):

  people = db.select(msg.from_user.id)

  await msg.answer(f'Твой баланс {people.money}')
