from aiogram.types import Message
from app.media.texts.texts import _ 
from aiogram.fsm.context import FSMContext
from app.States.fsm_add_client import ClientINFO


async def add_client_func(msg:Message, state:FSMContext):
    await state.set_state(ClientINFO.name)
    await msg.answer(text=await _("add_client_text","ru"))

async def clientname_handler(msg:Message, state:FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(ClientINFO.contact)
    await msg.answer(text='Напиши теперь его контакт в телеграмме через @ или телефон +')

async def clientcontact_handler(msg:Message, state:FSMContext):
    await state.update_data(contact=msg.text)
    await state.set_state(ClientINFO.service)
    await msg.answer(text='Какую он услугу хочет?')

async def clientservice_handler(msg:Message, state:FSMContext):
    await state.update_data(service=msg.text)
    await state.set_state(ClientINFO.money)
    await msg.answer(text='Сколько можно взять денег?')

async def clientfrom_handler(msg:Message, state:FSMContext):
    await state.update_data(money=msg.text)
    await state.set_state(ClientINFO.client_from)
    await msg.answer(text='Откуда клиент?')

async def clientstatus_handler(msg:Message, state:FSMContext):
    await state.update_data(client_from=msg.text)
    await state.set_state(ClientINFO.client_status)
    await msg.answer(text='Какой сейчас этап сделки?')

async def finish_ac_func(msg:Message, state:FSMContext):
    await state.update_data(client_status=msg.text)
    datastate = await state.get_data()
    print(datastate)