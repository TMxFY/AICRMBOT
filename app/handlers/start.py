from aiogram.types import Message

async def start_func(msg:Message):
    await msg.answer(text="Привет")