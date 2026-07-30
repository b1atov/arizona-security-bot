from aiogram import types
import os

async def subscribe_kb():
    keyboard = types.InlineKeyboardMarkup()

    buttons = [
        types.InlineKeyboardButton(text="Подписаться", url=f"https://t.me/{os.getenv("channel_username")}"),
        types.InlineKeyboardButton(text="Проверить подписку", callback_data="sub_check")
    ]

    return keyboard.add(*buttons)