from aiogram import types

async def get_start_keyboards():
    reply_kb = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton("Начать")],
        [types.KeyboardButton("Узнать ID профиля"), types.KeyboardButton("Дополнительные рассылки")]
    ])
    inline_kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Получить код", callback_data="get_code"))

    return reply_kb, inline_kb