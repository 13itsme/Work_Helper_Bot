import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from config.config import TOKEN, DATABASE_URL
from models import Base
from core import router, async_session, engine
import handlers.handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())