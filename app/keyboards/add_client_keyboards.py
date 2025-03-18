from aiogram import types 
from aiogram.types import InlineKeyboardButton as button
from app.media.texts.texts import _
from app.db import get_all_status,get_all_froms

async def finishaddclient():
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [button(text=await _('add_client_bt_yes','ru'),callback_data='Yes(add_client)'),
         button(text=await _('add_client_bt_no','ru'),callback_data='No(add_client)')],
        [button(text=await _('add_client_bt_delete','ru'),callback_data='Delete(add_client)')]
    ])
    return ikb

async def changedata_addclient(data:dict):
    clientparametr = {
        "name":'Имя',
        "contact":'Контакт',
        "service":'Услуга',
        "money":'Деньги',
        "client_from":'Откуда',
        "client_status":'Статус',
    }
    buttons = [button(text=clientparametr[k], callback_data=f"{k}-change(add_client)") for k in data]
    keyboardfinal = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboardfinal)

async def clientstatuskb(session_maker):
    func:list = await get_all_status(session_maker)
    buttons = [button(text=func[i]["status"],callback_data=f'{func[i]['status_id']}_{func[i]['status']}_(add_client)') for i in range(len(func))]
    keyboardfinal = [buttons[i:i+3] for i in range(0, len(buttons), 3)]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboardfinal)

async def clientfromkb(session_maker):
    func:list = await get_all_froms(session_maker)
    buttons = [button(text=func[i]["clientfrom"],callback_data=f'{func[i]['from_id']}_{func[i]['clientfrom']}_(add_client)') for i in range(len(func))]
    keyboardfinal = [buttons[i:i+3] for i in range(0, len(buttons), 3)]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboardfinal)