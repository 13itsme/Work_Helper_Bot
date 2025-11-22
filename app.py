import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from models import Base
from core import router, async_session, engine
import handlers.handlers

TOKEN = os.getenv("BOT_TOKEN")
LOCAL_DB = 'sqlite+aiosqlite:///./database/workhelper.db'
DATABASE_URL = os.getenv("DATABASE_URL", LOCAL_DB)

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