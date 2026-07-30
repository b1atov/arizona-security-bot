from main import bot, dp
from aiogram import types
from keyboards.start_kb import get_start_keyboards
from keyboards.other import subscribe_kb
from utils.check_subscribe import check_subscribe
import os

@dp.message_handler()
async def main_handler(message: types.Message):
    text = message.text

    if text == "Начать": 
        await start_message(message)

    elif text == "Узнать ID профиля":
        text = (
            f"🔘 Ваш ID Telegram профиля: <code>{message.from_user.id}</code>\n\n"
            f"ℹ️ Данный идентификатор используется при восстановлении пароля от игрового аккаунта."
        )
        await message.answer(text)

    elif text == "Дополнительные рассылки":
        text = (
            "❌ В данный момент Вы не подписаны на дополнительные новостные и акционные рассылки.\n\n"
            "⚠️ Вы упускаете возможность быть в курсе всех новостей и акций!"
        )
        return await message.answer(text)

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await message.delete()
    reply_kb, inline_kb = await get_start_keyboards()

    is_subscribed = await check_subscribe(message.from_user.id)
    if not is_subscribed:
        inline_kb = await subscribe_kb()

    text = (
        "С помощью данного бота Вы сможете обезопасить свой игровой аккаунт от взлома и восстановить его в случае утраты пароля."
        "Для привязки игрового аккаунта, воспользуйтесь кнопкой «Получить код»"
        f"Перед началом взаимодействия, необходимо подписаться на наш новостной канал @{os.getenv("channel_username")}."
    )

    await bot.send_message(message.chat.id, "👋", reply_markup=reply_kb)
    await bot.send_message(message.chat.id, text, reply_markup=inline_kb)