from aiogram import types 
from aiogram.types import InlineKeyboardButton as button
from app.media.texts.texts import _


async def start_kb():
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [button(text='Добавить клиента',callback_data='Add(add_client)'),
         button(text='Просмотров клиентов',callback_data='Main(lookup_client)')],
        [button(text='Статистика',callback_data='Main(statistics)'),
         button(text='Анализ клиента',callback_data='Main(analyzeclient)')],
    ])
    return ikb