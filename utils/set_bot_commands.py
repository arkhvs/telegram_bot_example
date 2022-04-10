from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('register', 'Регистрация'),
        types.BotCommand('photo', 'Фотография'),
        types.BotCommand('album', 'Альбом фотографий')
    ])
