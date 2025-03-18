from aiogram.types import Message
from app.media.texts.texts import _ 
from app.keyboards import start_kb
from aiogram.fsm.context import FSMContext

async def start_func(msg:Message, state:FSMContext,session_maker):
    await state.clear()
    await msg.answer(text=await _('start_text','ru'),reply_markup=await start_kb())