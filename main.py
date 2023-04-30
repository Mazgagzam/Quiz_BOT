import asyncio

import logging

from aiogram import Bot, Dispatcher

from handlers import register_func

from database.database_class import DataBase

from database.db_arg import db

from learn_maks import *

logging.basicConfig(level=logging.INFO)

async def main():

    bot = Bot(token="TOKEN", parse_mode = 'html')

    dp = Dispatcher(bot)

    register_func(dp)

  

    await dp.start_polling()

   

def cli():

    try:

        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):

        print('BOT STOPPED')

if __name__ == '__main__':

    cli()
