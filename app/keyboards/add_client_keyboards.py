from aiogram import types 
from aiogram.types import InlineKeyboardButton as button
from app.media.texts.texts import _


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
    buttons = [button(text=clientparametr[k], callback_data=f"{k}-change") for k in data]
    keyboardfinal = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboardfinal)

# print(changedata_addclient({'name': 'asdfkjh', 'contact': 'askdjfh', 'service': 'asdkfjh', 'money': 'sadfkjh', 'client_from': 'sdkjfh', 'client_status': 'sdkfjh'}))