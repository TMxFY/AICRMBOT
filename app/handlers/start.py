from aiogram.types import Message
from app.media.texts.texts import _ 

async def start_func(msg:Message):
    await msg.answer(text=await _('start_text','ru'))