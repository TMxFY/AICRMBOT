from aiogram import Bot, Dispatcher
import logging
import os
from sqlalchemy.engine import URL
from app.db import create_async_engine, get_session_maker
import asyncio
from app.handlers import register_user_handlers
from os import getenv as ge
import pathlib
from redis.asyncio import Redis
redis = Redis(host=ge("REDIS_HOST"), port=ge("REDIS_PORT"), db=ge("REDIS_DB"))

print(ge('bot_token'))
async def bot_start(logger):
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=ge('bot_token'))
    dp = Dispatcher()
    register_user_handlers(dp)
    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=ge("POSTGRES_USER"),
        host=ge("POSTGRES_HOST"),
        database=ge("POSTGRES_DB"),
        port=ge("POSTGRES_PORT"),
        password=ge("POSTGRES_PASSWORD")
    )
    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await dp.start_polling(bot, session_maker=session_maker,redis=redis,logger=logger)


def setup_env():
    """Настройка переменных окружения"""
    from dotenv import load_dotenv
    path = pathlib.Path(__file__).parent.parent
    dotenv_path = path.joinpath('.env')
    if dotenv_path.exists():
        load_dotenv(dotenv_path)


def main():
    """Функция для запуска через poetry"""
    logger = logging.getLogger(__name__)
    try:
        setup_env()
        asyncio.run(bot_start(logger))
        logger.info('Bot started')
    except (KeyboardInterrupt, SystemExit):
        logger.info('Bot stopped')
    
if __name__ == '__main__':
    main()


