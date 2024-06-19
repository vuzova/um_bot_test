import asyncio

from config import TOKEN
from aiogram import Bot, Dispatcher

import logging

from app.handlers import router
from app.database.models import async_main

from app.middlewares.auth_middleware import AuthMiddleware
from app.middlewares.registration_middleware import RegistrationMiddleware

async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.message.middleware(AuthMiddleware())
    dp.message.middleware(RegistrationMiddleware())
    await dp.start_polling(bot)

if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
