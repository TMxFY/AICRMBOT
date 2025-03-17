from aiogram.types import Message
from app.media.texts.texts import _ 
from aiogram.fsm.context import FSMContext
from app.States.fsm_add_client import ClientINFO
from app.keyboards import finishaddclient 

# Указываем порядок состояний для последовательного ввода данных
STATES_ORDER = {
    ClientINFO.name: ("name", "add_client_contact", ClientINFO.contact),
    ClientINFO.contact: ("contact", "add_client_service", ClientINFO.service),
    ClientINFO.service: ("service", "add_client_money", ClientINFO.money),
    ClientINFO.money: ("money", "add_client_from", ClientINFO.client_from),
    ClientINFO.client_from: ("client_from", "add_client_status", ClientINFO.client_status),
    ClientINFO.client_status: ("client_status", "add_client_finish", None)  # Последнее состояние
}

numberoffileds = len(STATES_ORDER)  # Динамически определяем количество полей

async def add_client_func(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ClientINFO.name)
    await msg.answer(text=await _("add_client_text", "ru"))

async def client_handler(msg: Message, state: FSMContext):
    """ Универсальный обработчик для всех состояний """
    current_state = await state.get_state()
    
    if current_state in STATES_ORDER:
        field, next_text, next_state = STATES_ORDER[current_state]
        await state.update_data(**{field: msg.text if field != "money" else int(msg.text)})
        data = await state.get_data()

        if len(data) == numberoffileds:  # Если все данные собраны, завершаем процесс
            text = await _("add_client_finish", "ru")
            await msg.answer(text=text.format(**data), reply_markup=await finishaddclient())
        else:
            await state.set_state(next_state)
            await msg.answer(text=await _(next_text, "ru"))
