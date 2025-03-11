from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class ClientINFO(StatesGroup):
    name = State()
    contact = State()
    service = State()
    money = State()
    client_from = State()
    client_status = State()

