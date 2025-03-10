all=['register_users_handler']

from aiogram import Router
from aiogram.filters import Command
from aiogram import F
import datetime 
from .start import start_func

def register_user_handlers(router:Router) -> None:
    router.message.register(start_func,Command(commands=['start']))