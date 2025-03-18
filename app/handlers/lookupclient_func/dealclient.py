from aiogram.types import Message
from app.media.texts.texts import _ 
from app.keyboards import start_kb
from app.db import get_all_clients
from aiogram.fsm.context import FSMContext

async def dealclient_func(msg:Message, state:FSMContext, session_maker):
    data:list = await get_all_clients(session_maker) #Добавить редис 
    args = msg.text.split(maxsplit=1)  # Разделяем команду и аргумент
    if len(args) < 2:
        await msg.answer("Ошибка: укажите аргумент. Пример: /deal contact")
        return
    argument = args[1]
    lisres = [i["contact"] for i in data]
    dictres = {i["contact"]:[i['name'],i['contact'],i['service'],i['money'],i['client_from'],i['client_status']] for i in data}
    text = await _('lookupclient(dealclient)','ru')
    text = text.format(name=dictres[argument][0],contact=dictres[argument][1],
                       service=dictres[argument][2],money=dictres[argument][3],
                       client_from=dictres[argument][4],client_status=dictres[argument][5])
    if argument in lisres:
        await msg.answer(text) #map преобразует в строку
    else:
        await msg.answer("Unknown user")
