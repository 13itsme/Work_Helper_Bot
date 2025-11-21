from core import router, async_session
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from models import Record
from lexicon.lexicon_en import LEXICON_EN
from aiogram.filters import Command

# Хендлер /start
@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(LEXICON_EN['start'])

@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer(LEXICON_EN['help'])