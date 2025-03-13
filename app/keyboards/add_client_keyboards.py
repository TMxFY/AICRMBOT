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