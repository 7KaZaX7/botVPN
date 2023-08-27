#from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_keyboard_main():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='👤Профиль')
    keyboard_builder.button(text='🆘Помощь')
    keyboard_builder.button(text='🎫Купить доступ')
    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup(resize_keyboard=True)


def reply_keyboard_admin_main():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='👤Профиль')
    keyboard_builder.button(text='🆘Помощь')
    keyboard_builder.button(text='🎫Купить доступ')
    keyboard_builder.button(text='↪️Рассылка')
    keyboard_builder.button(text='Отправить пользователю')
    keyboard_builder.adjust(2, 1, 2)
    return keyboard_builder.as_markup(resize_keyboard=True)


def reply_keyboard_cancel():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='❌Отмена')
    return keyboard_builder.as_markup(resize_keyboard=True)

# reply_keyboard_main = ReplyKeyboardMarkup(keyboard=[
#     [
#         KeyboardButton(
#             text='Помощь'
#         ),
#         KeyboardButton(
#             text='Купить доступ'
#         )
#     ],
#     [
#         KeyboardButton(
#             text='Помощь'
#         ),
#         KeyboardButton(
#             text='Купить доступ'
#         )
#     ]
# ],
# resize_keyboard=True)