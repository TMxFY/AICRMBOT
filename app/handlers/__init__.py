all=['register_users_handler']

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram import F
import datetime 
from app.States.fsm_add_client import ClientINFO
from .start_func.start import start_func
from .add_client_func.add_client import *
from .add_client_func.add_client_query import *
from .lookupclient_func.lookupclient_query import *
from .analyzeclient_func.aianalyzeclient_query import *
from .statistics_query.statistics_query import *
from .lookupclient_func.dealclient import *


def register_user_handlers(router:Router) -> None:
    router.message.register(start_func,Command(commands=['start']))
    router.message.register(add_client_func,Command(commands=['add_client']))
    for i in ['name','contact','service','money','client_from','client_status']:
        router.message.register(client_handler,StateFilter(getattr(ClientINFO,i)))
    router.callback_query.register(add_client_query,F.data.endswith("(add_client)")) #добавить обработчики
    router.callback_query.register(lookup_query,F.data.endswith("(lookup_client)"))
    router.callback_query.register(statistics_query,F.data.endswith("(statistics)"))
    router.callback_query.register(aianalyzeclient_query,F.data.endswith("(analyzeclient)"))
    router.message.register(dealclient_func,Command(commands=['deal']))


