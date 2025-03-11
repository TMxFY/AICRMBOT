all=['register_users_handler']

from aiogram import Router
from aiogram.filters import Command
from aiogram import F
import datetime 
from app.States.fsm_add_client import ClientINFO
from .start import start_func
from .add_client import *

def register_user_handlers(router:Router) -> None:
    router.message.register(start_func,Command(commands=['start']))
    router.message.register(add_client_func,Command(commands=['add_client']))
    router.message.register(clientname_handler,ClientINFO.name)
    router.message.register(clientcontact_handler,ClientINFO.contact)
    router.message.register(clientservice_handler,ClientINFO.service)
    router.message.register(clientfrom_handler,ClientINFO.money)
    router.message.register(clientstatus_handler,ClientINFO.client_from)
    router.message.register(finish_ac_func,ClientINFO.client_status)

