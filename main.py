import platform
"""------------------------>aiogram imports<------------------------"""
from aiogram import Dispatcher
from aiogram.types import ContentType
from aiogram.filters import Command, ContentTypesFilter
from aiogram import F

"""------------------------>project imports<------------------------"""

from core.handlers.basic import *
from core.handlers.callback import select_access
from core.settings import settings
from core.untils.commands import set_commands
from core.untils.statesall import *


"""------------------------>other imports<------------------------"""

import asyncio
import logging


"""------------------------>user/bot move register<------------------------"""


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot start')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot stop')


"""------------------------>main start function<------------------------"""


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_help, (Command(commands=['help'])) | (F.text == '🆘Помощь'))
    dp.message.register(get_inline, Command(commands=['access']))

    dp.message.register(get_help_answer, contact.support_request)
    dp.message.register(set_admin_message, admin_message.push)
    dp.message.register(set_admin_message, admin_message.set_id)
    dp.message.register(set_admin_message, admin_message.set_message)

    dp.message.register(get_profile, F.text == '👤Профиль')
    dp.message.register(get_inline, F.text == '🎫Купить доступ')
    dp.message.register(get_admin_message, (F.text == '↪️Рассылка') | (F.text == 'Отправить пользователю'))
    dp.message.register(get_photo, F.photo)

    # dp.pre_checkout_query.register(pre_checkout_query)
    # dp.message.register(successuful_payment, ContentTypesFilter(content_types=[ContentType.SUCCESSFUL_PAYMENT]))

    dp.callback_query.register(select_access)

    dp.message.register(get_trash)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


"""------------------------>run bot<------------------------"""

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(start())
