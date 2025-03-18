from aiogram.types import Message,CallbackQuery
from app.media.texts.texts import _ 
from aiogram.fsm.context import FSMContext
from app.States.fsm_add_client import ClientINFO
from app.db import create_client, get_all_status, get_all_froms
from app.keyboards import changedata_addclient as chgad 
from app.keyboards import finishaddclient, clientstatuskb

async def add_client_query(msg:CallbackQuery,state:FSMContext,session_maker):
    data = await state.get_data()
    func:list = await get_all_status(session_maker) #в редис
    func2:list = await get_all_froms(session_maker)
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
    if msg.data in [f'{func[i]['status_id']}_{func[i]['status']}_(add_client)' for i in range(len(func))]:
        #либо словарь либо обращение к базе данных
        await state.update_data(client_status=int(msg.data.split('_')[0]))
        data = await state.get_data()
        text = await _("add_client_finish", "ru")
        data.pop("client_status", None)
        await msg.message.edit_text(text=text.format(**data,client_status=msg.data.split('_')[1]), reply_markup=await finishaddclient())
    if msg.data in [f'{func2[i]['from_id']}_{func2[i]['clientfrom']}_(add_client)' for i in range(len(func2))]:
        await state.update_data(client_from=int(msg.data.split('_')[0]))
        data = await state.get_data()
        if len(data) == 6:
            data.pop("client_from", None)
            text = await _("add_client_finish", "ru")
            await msg.message.edit_text(text=text.format(**data,client_from=msg.data.split('_')[1]), reply_markup=await finishaddclient())
        else:
            text = await _("add_client_status", "ru")
            await msg.message.edit_text(text=text, reply_markup=await clientstatuskb(session_maker))

## все увидишь когда запустишь бота