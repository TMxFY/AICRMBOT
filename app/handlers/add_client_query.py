from aiogram.types import Message,CallbackQuery
from app.media.texts.texts import _ 
from aiogram.fsm.context import FSMContext
from app.States.fsm_add_client import ClientINFO

async def add_client_query(msg:CallbackQuery,state:FSMContext):
    print(msg.data)
    if msg.data == 'Yes(add_client)':
        await msg.message.edit_text(text='Hi there')
    if msg.data == 'No(add_client)':
        await msg.message.edit_text(text='Hi there2')
    if msg.data == 'Delete(add_client)':
        await msg.message.edit_text(text='Hi there3')
        await state.clear()
