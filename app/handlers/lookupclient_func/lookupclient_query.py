from aiogram.types import Message,CallbackQuery
from app.media.texts.texts import _ 
from aiogram.fsm.context import FSMContext
from app.States.fsm_add_client import ClientINFO
from app.db import get_all_clients
from app.keyboards import * 

async def lookup_query(msg:CallbackQuery,state:FSMContext,session_maker):
    if msg.data == 'Main(lookup_client)':
        data:list = await get_all_clients(session_maker)
        text,text2 = await _('lookupquerymain','ru'), await _('lookupquerymain(addition)','ru')
        result_text="".join(reversed([text.format(**data[i]) for i in range(len(data))]))
        await msg.message.edit_text(text=f"{result_text}{text2}")