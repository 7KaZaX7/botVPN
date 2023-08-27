"""------------------------>aiogram imports<------------------------"""

from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

"""------------------------>project imports<------------------------"""

from core.keyboards.reply import *
from core.untils.statesall import *
from core.keyboards.inline import *

"""------------------------>all callback function<------------------------"""


async def select_access(call: CallbackQuery, bot: Bot, state: FSMContext):
    if call.data == 'acc_1':
        await bot.edit_message_text('<b>Вы выбрали доступ на 3 дня.</b>\n'
                                    '\nВы получите личный VPN в Нидерландах '
                                    'с максимальной скоростью работы и надежной '
                                    'зашитой ваших данных, без ограничений по трафику.'
                                    ' Всего за <b>20 руб.</b>',
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=inline_keyboard_payment())

    elif call.data == 'acc_4':
        await bot.edit_message_text('<b>Вы выбрали доступ на 30 дней.</b>\n'
                                    '\nВы получите личный VPN в Нидерландах '
                                    'с максимальной скоростью работы и надежной '
                                    'зашитой ваших данных, без ограничений по трафику.'
                                    ' Всего за <b>150 руб.</b>',
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=inline_keyboard_payment())

    elif call.data == 'acc_2':
        await bot.edit_message_text('<b>Вы выбрали доступ на 7 дней.</b>\n'
                                    '\nВы получите личный VPN в Нидерландах '
                                    'с максимальной скоростью работы и надежной '
                                    'зашитой ваших данных, без ограничений по трафику.'
                                    ' Всего за <b>40 руб.</b>',
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=inline_keyboard_payment())

    elif call.data == 'acc_3':
        await bot.edit_message_text('<b>Вы выбрали доступ на 15 дней.</b>\n'
                                    '\nВы получите личный VPN в Нидерландах '
                                    'с максимальной скоростью работы и надежной '
                                    'зашитой ваших данных, без ограничений по трафику. '
                                    'Всего за <b>80 руб.</b>',
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=inline_keyboard_payment())

    elif call.data == 'acc_5':
        await bot.edit_message_text('<b>Вы выбрали доступ на 60 дней.</b>\n'
                                    '\nВы получите личный VPN в Нидерландах '
                                    'с максимальной скоростью работы и надежной '
                                    'зашитой ваших данных, без ограничений по трафику.'
                                    ' Всего за <b>280 руб.</b>',
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=inline_keyboard_payment())
    await call.answer()

    if call.data == 'support':
        await state.set_state(contact.support_request)
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id,
                               'Задайте свой вопрос мне, я его передам.',
                               reply_markup=reply_keyboard_cancel())
        await call.answer()

    if call.data == 'pay':
        await bot.send_message(call.from_user.id, f'Для покупки свяжитесь с администратором @thisistheobserver')
        await call.answer()

    if call.data == 'free':
        await bot.send_message(call.from_user.id, f'Вам разрешен бесплатный доступ, скорее пишите @thisistheobserver, '
                                                  f'чтобы получить VPN в Нидерландах!')

    if call.data == 'cancel':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id, 'Отмена успешна', reply_markup=reply_keyboard_main())
        await state.clear()
        await call.answer()
