from core import router, async_session
from aiogram import F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from models import Record
from lexicon.lexicon_en import LEXICON_EN
from aiogram.filters import Command, StateFilter
from sqlalchemy import select, delete
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class DeleteAllStates(StatesGroup):
    waiting_for_confirmation = State()


# Хендлер /start
@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(LEXICON_EN['start'])


# Хендлер /help
@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer(LEXICON_EN['help'])


# Хендлер /add + добавление записи в БД
@router.message(Command('add'))
async def add_command(message: Message):
    format_message = message.text.split()

    if len(format_message) < 3:
        await message.reply("Please, send me correct format:\n/add [video's title] [cost]")
        return

    title = " ".join(format_message[1:-1])

    try:
        cost = int(format_message[-1])
    except ValueError:
        await message.reply("Cost should be a number!")
        return

    if len(title) > 20:
        await message.reply("Title is too long. Max 20 characters.")
        return

    async with async_session() as session:
        existing = await session.execute(
            select(Record).where(Record.title == title)
        )
        if existing.scalars().first():
            await message.reply("This video already exists in the database")
            return

        new_record = Record(title=title, cost=cost)
        session.add(new_record)
        await session.commit()

        result = await session.execute(select(Record.cost))
        all_costs = result.scalars().all()
        total = sum(all_costs)

    await message.answer(f"Video successfully added!\nCurrent total sum of all videos: {total}$")

# Хендлер /sum
@router.message(Command('sum'))
async def sum_command(message: Message):
    async with async_session() as session:
        db = await session.execute(select(Record.cost))
        costs = db.scalars().all()
        total = sum(costs)

    await message.answer(LEXICON_EN['sum'].format(total=total))

# Хендлер /list
@router.message(Command('list'))
async def list_command(message: Message):
    async with async_session() as session:
        db = await session.execute(select(Record.title, Record.cost))
        rows = db.all()
        videos_list = "\n".join(f'{title} - {cost}$' for title, cost in rows)

    await message.answer(LEXICON_EN['list'].format(videos_list=videos_list))

# Хендлер /edit
@router.message(Command('edit'))
async def edit_command(message: Message):
    format_message = message.text.split()

    if len(format_message) < 5:
        await message.answer("Incorrect format, send like this:\n/edit [old title] [old cost] [new title] [new cost]")
        return

    old_title = format_message[1]
    try:
        old_cost = int(format_message[2])
    except ValueError:
        await message.reply('Old number must be a number!')
        return

    new_title = format_message[3]
    try:
        new_cost = int(format_message[4])
    except ValueError:
        await message.reply('New cost must be a number!')
        return

    async with async_session() as session:
        result = await session.execute(
            select(Record).where(Record.title == old_title, Record.cost == old_cost)
        )
        record = result.scalars().first()

        if not record:
            await message.answer('Record not found')
            return

        record.title = new_title
        record.cost = new_cost

        await session.commit()

    await message.answer(f"Record successfully updated: {new_title} - {new_cost}$")

# Хендлер /delete
@router.message(Command('delete'))
async def delete_command(message: Message):
    format_message = message.text.split()

    if len(format_message) < 2:
        await message.reply(f'Please, send correct format:\n/delete [title]')
        return

    title = " ".join(format_message[1:])

    async with async_session() as session:
        result = await session.execute(
            select(Record).where(Record.title == title)
        )
        record = result.scalars().first()

        if not record:
            await message.reply('Video not found')
            return

        await session.delete(record)
        await session.commit()
        await message.answer('Video Successfully deleted')

# Хендлер /delete_all
@router.message(Command('delete_all'))
async def delete_all_command(message: Message, state: FSMContext):
    await message.answer('Are you sure that you want to delete all videos from database?\nSend Y/N')
    await state.set_state(DeleteAllStates.waiting_for_confirmation)
@router.message(DeleteAllStates.waiting_for_confirmation, F.text.lower().in_({'y', 'n'}))
async def delete_all_confirmation(message: Message, state: FSMContext):
    user_reply = message.text.lower().strip()

    if user_reply == 'y':
        async with async_session() as session:
            await session.execute(delete(Record))
            await session.commit()
        await message.answer('All videos have been deleted.')
    if user_reply == 'n':
        await message.answer('Operation cancelled')
    else:
        await message.answer('Sorry, you should have send me Y or N.\nIf you want to continue, send me /delete_all one more time')

    await state.clear()
