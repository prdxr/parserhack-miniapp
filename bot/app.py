from aiogram import executor
from dotenv import load_dotenv
from handlers.users import *
from handlers.on_start import start
from handlers.on_shutdown import shutdown


if __name__ == "__main__":
    load_dotenv()
    executor.start_polling(dp, on_startup=start, 
                           on_shutdown=shutdown)
