import random

from aiogram import types, bot

from database.db_arg import db

async def get_dice(msg: types.Message):  

  db.new_people(msg)

  if msg.dice.emoji != '🎲':

    await msg.answer('Нужно отправить 🎲')

    return None



  people = db.select(msg.from_user.id)

  if people.money > 0 and  msg.dice.value >= 4:

    money = random.randint(1,100)

    await msg.reply(f"Ты выиграл {money}")

  elif people.money > 0:

    money = random.randint(-people.money,-1) if people.money <= 100 else random.randint(-100,-1)

    await msg.reply(f"Ты приграл {money}")

  else:

    await msg.answer('У вас не хватает денег')



  people.money += money

  people.save_people(db)
