from main import bot
import os
import logging

async def check_subscribe(userId) -> bool:
    try: 
        member = await bot.get_chat_member(chat_id=int(os.getenv("channel_id")), user_id=userId)
        return member.status in ["creator", "administrator", "member", "restricted"]
    except Exception:
        logging.exception("check_subscribe failed")
        return False
