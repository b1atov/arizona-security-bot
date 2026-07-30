from aiogram import Dispatcher, Bot, executor
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv("bot_token"))
dp = Dispatcher(bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

