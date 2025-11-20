import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from config.config import TOKEN, DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Асинхронный движок SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Фабрика сессий для работы с базой
# noinspection PyTypeChecker
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_db()
    await dp.start_polling()

if __name__=='__main__':
    asyncio.run(main())