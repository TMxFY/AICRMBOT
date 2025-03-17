from aiogram.types import Message,CallbackQuery
from app.media.texts.texts import _ 
from aiogram.fsm.context import FSMContext
from app.States.fsm_add_client import ClientINFO
from app.db import get_all_clients
from app.keyboards import * 

async def statistics_query(msg:CallbackQuery,state:FSMContext,session_maker):
    if msg.data == 'Main(statistics)':
        print('Main(statistics)')