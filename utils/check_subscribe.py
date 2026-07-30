from aiogram import types
from main import bot
import os

async def check_subscribe(userId) -> bool:
    try: 
        member = await bot.get_chat_member(chat_id=int(os.getenv("channel_id")), user_id=userId)
        return member.status in ["creator", "administrator", "member"]
    except Exception:
        return False