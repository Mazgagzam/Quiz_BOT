from aiogram import Dispatcher

from aiogram import types

from .start import start

from .random_num import random_num

from .all_msg import all_msg

from .callback import send_random_value

from .get_dice import get_dice

def register_func(dp: Dispatcher):

  dp.register_message_handler(

        start, commands = ["start"]

    )

  dp.register_message_handler(

    random_num, commands = ['random']

  )

  dp.register_message_handler(

    get_dice, content_types = ['dice']

  )

  

  dp.register_message_handler(all_msg)

  dp.register_callback_query_handler(send_random_value)
