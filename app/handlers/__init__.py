all=['register_users_handler']

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram import F
import datetime 
from app.States.fsm_add_client import ClientINFO
from .start import start_func
from .add_client import *
from .add_client_query import *

def register_user_handlers(router:Router) -> None:
    router.message.register(start_func,Command(commands=['start']))
    router.message.register(add_client_func,Command(commands=['add_client']))
    for i,y in zip(['name','contact','service','money','client_from','client_status'],[clientname_handler,clientcontact_handler,clientservice_handler,clientfrom_handler,clientstatus_handler,finish_ac_func]):
        router.message.register(y,StateFilter(getattr(ClientINFO,i))) # state filter регистрирует обработчик для каждого аргумента
    router.callback_query.register(add_client_query)
