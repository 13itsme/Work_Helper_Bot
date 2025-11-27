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

async def set_bot_commands():
    """Bot's menu commands"""
    commands = [
        types.BotCommand(command='start', description='Start the bot'),
        types.BotCommand(command='help', description='Het help'),
        types.BotCommand(command='add', description='Add video [title] [cost]'),
        types.BotCommand(command='list', description='Show all videos'),
        types.BotCommand(command='sum', description='Show total sum of videos'),
        types.BotCommand(command='edit', description='Edit video in list'),
        types.BotCommand(command='delete', description='Delete video from list'),
        types.BotCommand(command='delete_all', description='Delete all videos from list'),
        types.BotCommand(command='exchange', description='Convert USD to any currency you want')
    ]


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_db()
    await set_bot_commands()
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())