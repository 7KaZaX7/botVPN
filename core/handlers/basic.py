"""------------------------>aiogram imports<------------------------"""

from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

"""------------------------>project imports<------------------------"""

from core.keyboards.reply import *
from core.keyboards.inline import *
from core.untils.databaze import *
from core.settings import settings
from core.untils.statesall import *

"""------------------------>all function<------------------------"""


async def get_start(message: Message, bot: Bot):
    if message.from_user.id == settings.bots.admin_id:
        await bot.send_message(message.from_user.id, f'Добро пожаловать мой властелин!',
                               reply_markup=reply_keyboard_admin_main())
        await get_profile(message, bot)
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, добро пожаловать!',
                               reply_markup=reply_keyboard_main())
        await get_profile(message, bot)
        await add_user(user_id=message.from_user.id)


async def get_help(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           '<b>Как происходит подключение?</b>\n'
                           'Всего 2 минуты, и VPN настроен и готов к работе.\n'
                           '<b>1.</b> Cкачайте приложение <b>Outline</b> на android, ios, windows, linux.\n'
                           '<b>2.</b> Aктивируйте свой доступ, который мы отправим вам после оплаты.\n'
                           '<i>P.S. После оплаты придет максимально подробная и '
                           'простая инструкция, а так же вы можете попросить помощи у продавца.</i>\n'
                           '\n<b>Есть ли ограничения по трафику?</b>\n'
                           'Нет! Нам и вам не нужны эти ограничения. '
                           'У нас идеальные условия:'
                           ' вам нужно один раз активировать доступ, '
                           'а потом навсегда о нем забыть. \n'
                           '\n<b>Что делать, если не работает?.</b>\n'
                           'Как у нас могут быть сбои, так и у '
                           'самих серверных отделов в Нидерландах. '
                           'Для таких случаев мы собрали техподдержку, '
                           'мы днем и ночью готовы решать любой ваш вопрос.\n'
                           '\n<b>Будут ли автоматически списываться деньги?</b>\n'
                           'Нет! Каждый раз вы лично выбираете срок использования VPN и '
                           'оплачиваете его самостоятельно.\n'
                           '\n<b>Не заблокируют ли VPN?</b>\n'
                           'Нет, не заблокируют. '
                           'Мы целенаправленно отказались от сайта и от приложения, '
                           'чтобы не привлекать лишнего внимания, '
                           'именно поэтому '
                           ' VPN можно купить дешевле.\n'
                           '\n<i>Первым 100 клиентам, '
                           'персональные подарки от администратора. '
                           'Не упускайте возможность купить VPN'
                           ' за копейки и получить '
                           'подарок.</i>',
                           reply_markup=inline_keyboard_help())


async def get_inline(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           'Выберите доступ, который вам подходит',
                           reply_markup=inline_keyboard_main())


async def get_profile(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           f'<b>Профиль</b>\n'
                           f'\n🦊Имя: {message.from_user.first_name} {message.from_user.last_name}\n'
                           f'\n👤\tПрофиль : @{message.from_user.username}\n'
                           f'\n#️⃣\tВаш айди : {message.from_user.id}\n'
                           f'\n🌍\tВаш язык : {message.from_user.language_code}\n'
                           f'\n\n<i>Если вам нужна помощь: /help</i>', reply_markup=inline_keyboard_free_access())


async def get_photo(message: Message, bot: Bot):
    await message.reply('Спасибо, эту фотографию я сохраню себе')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.forward_message(settings.bots.feedback_id, message.from_user.id, message.message_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_admin_message(message: Message, bot: Bot, state: FSMContext):
    if message.from_user.id == settings.bots.admin_id:
        if message.text == '↪️Рассылка':
            await message.reply('Хорошо, скажите, что мне нужно разослать', reply_markup=reply_keyboard_cancel())
            await state.set_state(admin_message.push)
        else:
            await message.reply('Хорошо, назовите ID пользователя', reply_markup=reply_keyboard_cancel())
            await state.set_state(admin_message.set_id)
    else:
        await message.reply('Извините, такое я еще не понимаю')


async def set_admin_message(message: Message, bot: Bot, state: FSMContext):
    if message.text != '❌Отмена':
        if await state.get_state() == 'admin_message:push':
            users = await get_users()
            for user in await users:
                try:
                    await bot.send_message(user[0], message.text)
                    if int(user[1]) != 1:
                        await set_active(user_id=user[0], active=1)
                except:
                    await set_active(user_id=user[0], active=0)
                await state.clear()

            await bot.send_message(message.from_user.id, 'Рассылка успешна!', reply_markup=reply_keyboard_admin_main())
            await state.clear()

        if await state.get_state() == 'admin_message:set_id':
            await state.update_data(set_id=message.text)
            await bot.send_message(message.from_user.id, 'Хорошо, скажите, что мне нужно отправить')
            await state.set_state(admin_message.set_message)

        elif await state.get_state() == 'admin_message:set_message':
            context_data = await state.get_data()
            id_user = context_data.get('set_id')
            await bot.send_message(int(id_user), message.text)
            await message.reply(f'Я отправил ваше сообщение пользователю: {id_user}!',
                                reply_markup=reply_keyboard_admin_main())
            await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Хорошо, рассылка успешно отменена!',
                               reply_markup=reply_keyboard_admin_main())
        await state.clear()


async def get_help_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text != '❌Отмена':
        await bot.forward_message(settings.bots.feedback_id, message.from_user.id, message.message_id)
        user_id = message.from_user.id
        await bot.send_message(chat_id=settings.bots.feedback_id, text=user_id)
        await message.reply('Вопрос получен, вам скоро ответят!', reply_markup=reply_keyboard_main())
    else:
        await message.reply('Хорошо, отправка сообщения в тех. поддержку отменена', reply_markup=reply_keyboard_main())
    await state.clear()


async def get_trash(message: Message, bot: Bot):
    await message.reply('Извините, такое я еще не понимаю')
