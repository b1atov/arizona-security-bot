from main import bot, dp
from aiogram import types
from keyboards.start_kb import get_start_keyboards
import os


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    reply_kb, inline_kb = await get_start_keyboards()

    text = f"""С помощью данного бота Вы сможете обезопасить свой игровой аккаунт от взлома и восстановить его в случае утраты пароля.
            Для привязки игрового аккаунта, воспользуйтесь кнопкой «Получить код»
            Перед началом взаимодействия, необходимо подписаться на наш новостной канал @{os.getenv("channel_username")}.
    """

    await bot.send_message(message.chat.id, "👋", reply_markup=reply_kb)
    await bot.send_message(message.chat.id, text, reply_markup=inline_kb)