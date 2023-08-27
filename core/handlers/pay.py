# from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
# from aiogram import Bot
#
# from core.settings import settings
#
#
# async def order_1(message: Message, bot: Bot):
#     await bot.send_invoice(
#         chat_id=message.chat.id,
#         title='Доступ на 3 дня',
#         description='Нидерландский сервер',
#         payload='получилось',
#         provider_token=settings.bots.payment_id,
#         currency='rub',
#         prices=[
#             LabeledPrice(
#                 label='Доступ на 3 дня',
#                 amount=15000
#             )
#         ],
#         start_parameter='nztcoder',
#         need_email=True
#     )
#
#
# async def order_2(message: Message, bot: Bot):
#     await bot.send_invoice(
#         chat_id=message.chat.id,
#         title='Доступ на 7 дней',
#         description='Нидерландский сервер',
#         payload='получилось',
#         provider_token=settings.bots.payment_id,
#         currency='rub',
#         prices=[
#             LabeledPrice(
#                 label='Доступ на 7 дней',
#                 amount=20000
#             )
#         ],
#         start_parameter='nztcoder',
#         need_email=True
#     )
#
#
# async def order_3(message: Message, bot: Bot):
#     await bot.send_invoice(
#         chat_id=message.chat.id,
#         title='Доступ на 15 дней',
#         description='Нидерландский сервер',
#         payload='получилось',
#         provider_token=settings.bots.payment_id,
#         currency='rub',
#         prices=[
#             LabeledPrice(
#                 label='Доступ на 15 дней',
#                 amount=40000
#             )
#         ],
#         start_parameter='nztcoder',
#         need_email=True
#     )
#
#
# async def order_4(message: Message, bot: Bot):
#     await bot.send_invoice(
#         chat_id=message.chat.id,
#         title='Доступ на 30 дней',
#         description='Нидерландский сервер',
#         payload='получилось',
#         provider_token=settings.bots.payment_id,
#         currency='rub',
#         prices=[
#             LabeledPrice(
#                 label='Доступ на 30 дней',
#                 amount=75000
#             )
#         ],
#         start_parameter='nztcoder',
#         need_email=True
#     )
#
#
# async def order_VIP(message: Message, bot: Bot):
#     await bot.send_invoice(
#         chat_id=message.chat.id,
#         title='Доступ навсегда',
#         description='Нидерландский сервер',
#         payload='получилось',
#         provider_token=settings.bots.payment_id,
#         currency='rub',
#         prices=[
#             LabeledPrice(
#                 label='Доступ навсегда',
#                 amount=60000
#             )
#         ],
#         start_parameter='nztcoder',
#         need_email=True
#     )
#
#
# async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
#     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
#
#
# async def successuful_payment(message: Message):
#     await message.answer(f'Спасибо за покупку, вот ваш файл')
