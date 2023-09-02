from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_keyboard_main():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='3 дня', callback_data='acc_1')
    keyboard_builder.button(text='7 дней', callback_data='acc_2')
    keyboard_builder.button(text='15 дней', callback_data='acc_3')
    keyboard_builder.button(text='30 дней', callback_data='acc_4')
    keyboard_builder.button(text='60 дней', callback_data='acc_5')
    
    keyboard_builder.adjust(3, 2)
    return keyboard_builder.as_markup()


def inline_keyboard_help():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Связаться с поддержкой', callback_data='support')
    return keyboard_builder.as_markup()


def inline_keyboard_payment():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Оплатить', callback_data='pay')
    keyboard_builder.button(text='❌Отмена', callback_data='cancel')
    return keyboard_builder.as_markup()


def inline_keyboard_free_access():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Попробовать VPN бесплатно🆓', callback_data='free')
    return keyboard_builder.as_markup()
