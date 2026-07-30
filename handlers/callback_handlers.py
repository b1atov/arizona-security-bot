from main import dp, bot
from aiogram import types
from utils.check_subscribe import check_subscribe
from database.redis import generate_code
from keyboards.other import subscribe_kb
from keyboards.start_kb import get_start_keyboards
import os

@dp.callback_query_handler()
async def callback_handler(callback: types.CallbackQuery):
    button = callback.data

    await callback.answer("")
    is_subscribed = await check_subscribe(callback.from_user.id)

    if button == "get_code":
        if not is_subscribed: 
            text = (
                "❌ Вы не подписаны на новостной канал undefined!\n\n"
                f"Чтобы привязать игровой аккаунта, подпишитесь: @{os.getenv("channel_username")}"
            )

            return await bot.send_message(callback.message.chat.id, text, reply_markup=await subscribe_kb())

        code, cooldown = await generate_code(callback.from_user.id)
        if not code:
            text = (
                "❌ Вы уже сгенерировали код привязки!\n\n" 
                f"Новый код можно будет получить через {cooldown} минут."
            )
            return await bot.send_message(callback.message.chat.id, text)

        text = (
            "Вы успешно создали заявку на привязку игрового аккаунта к Telegram.\n\n"
            f"🔒 Ваш код для привязки: <code>{code}</code>\n\n"
            "Сейчас вам нужно скопировать данный код и вставить его в диалоге с привязкой аккаунта в игре.\n"
            "Код действителен в течении 10-ти минут.\n\n"
            "Подробная инструкция для привязки игрового аккаунта:\n"
            "1️⃣ Зайдите в игру под свой игровой аккаунт;\n"
            "2️⃣ Откройте /mn — Личные настройки — Защита VK / Telegram — Привязка Telegram;\n"
            "3️⃣ Выберите пункт 'Привязать аккаунт';\n"
            "4️⃣ Введите указанный код для привязки.\n\n"
            "☑️ Если Вы сделали все по инструкции, тогда бот пришлет вам уведомление об успешной привязке аккаунта."
        )

        return await bot.send_message(callback.message.chat.id, text)    

    if button == "sub_check":
        if not is_subscribed:
            await callback.message.copy_to(chat_id=callback.message.chat.id)
        else:
            _, inline_kb = await get_start_keyboards()
            text = "✅ Теперь Вы можете начать привязку игрового аккаунта!"

            return await bot.send_message(callback.message.chat.id, text, reply_markup=inline_kb)