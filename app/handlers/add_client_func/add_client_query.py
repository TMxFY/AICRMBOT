from aiogram.types import Message,CallbackQuery
from app.media.texts.texts import _ 
from aiogram.fsm.context import FSMContext
from app.States.fsm_add_client import ClientINFO
from app.db import create_client
from app.keyboards import changedata_addclient as chgad 

async def add_client_query(msg:CallbackQuery,state:FSMContext,session_maker):
    data = await state.get_data()
    if msg.data == 'Yes(add_client)':
        await msg.message.edit_text(text=await _("add_client_bd_add",'ru'))
        await create_client(**data,session_maker=session_maker)
        await state.clear()
    if msg.data == 'No(add_client)':
        await msg.message.edit_text(text=await _("add_client_no_change",'ru'),reply_markup=await chgad(data))
    if msg.data == 'Delete(add_client)':
        await msg.message.edit_text(text=await _("add_client_del",'ru'))
        await state.clear()
    if msg.data in [f"{k}-change(add_client)" for k,y in data.items()]:
        await msg.message.edit_text(text="Напиши новое значение")
        dataupdated = str(msg.data).split('-')[0]
        await state.set_state(getattr(ClientINFO,dataupdated))
    if msg.data == 'Add(add_client)':
        await state.clear()
        await state.set_state(ClientINFO.name)
        await msg.message.edit_text(text=await _("add_client_text", "ru"))
        