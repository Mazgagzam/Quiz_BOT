from aiogram import Dispatcher

from aiogram.types import Message

from database.db_arg import db

async def start(msg: Message):

  global db

  db.new_people(msg)

  people = db.select(msg.from_user.id)

  print(db.read_table())

  

  await msg.reply(f"Hello, {msg.from_user.first_name}!")

  await msg.answer(

    f'Your user {people.user}'

  )

  people.user = None

  people.save_people(db)
