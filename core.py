from aiogram import Router, F
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

router = Router()

LOCAL_DB = 'sqlite+aiosqlite:///./database/workhelper.db'

# База для деплоя
DATABASE_URL = os.getenv('DATABASE_URL', LOCAL_DB)

# Асинхронный движок SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Фабрика сессий для работы с базой
# noinspection PyTypeChecker
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)