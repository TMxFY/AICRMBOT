from aiogram.types import Message,CallbackQuery
from app.media.texts.texts import _ 
from aiogram.fsm.context import FSMContext
from app.States.fsm_add_client import ClientINFO
from app.db import count_all_clients
from app.keyboards import * 

async def statistics_query(msg:CallbackQuery,state:FSMContext,session_maker):
    if msg.data == 'Main(statistics)':
        func = await count_all_clients(session_maker)
        text=await _('statisticsmain(statistics)','ru')
        text=text.format(sumcl=sum(func[0]),clients=len(func[1]))
        await msg.message.edit_text(text=text)