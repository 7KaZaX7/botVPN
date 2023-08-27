from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запуск/Перезапуск бота'
        ),
        BotCommand(
            command="help",
            description="Часто задаваемые вопросы/Cвязаться с поддержкой"
        ),
        BotCommand(
            command='access',
            description='Выбрать доступ'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
