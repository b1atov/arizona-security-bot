from aiogram import Dispatcher, Bot, executor
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv("bot_token"), parse_mode="HTML")
dp = Dispatcher(bot)

if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp, skip_updates=False)

