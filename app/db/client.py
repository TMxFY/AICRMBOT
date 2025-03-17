from sqlalchemy.exc import ProgrammingError
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, select, BigInteger, DateTime  # type: ignore
from .base import Base   
from sqlalchemy.orm import sessionmaker
from redis.asyncio.client import Redis

class Client(Base):
    __tablename__ = 'client'
    client_id = Column(BigInteger, unique=True, nullable=False, primary_key=True,autoincrement="auto")
    name = Column(VARCHAR(255), nullable=False)
    contact = Column(VARCHAR(255), nullable=False)
    service = Column(VARCHAR(255), nullable=False) #сделать потом выпадающий список
    money = Column(Integer, nullable=False)
    client_from = Column(VARCHAR(255), nullable=False)
    client_status = Column(VARCHAR(255), nullable=False) #сделать потом выпадающий список

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


async def create_client(name:str,
                        contact:str,
                        service:str,
                        money:int,
                        client_from:str,
                        client_status:str,
                        session_maker: sessionmaker,):
    async with session_maker() as session:
        async with session.begin():
            client = Client(
                name=name,
                contact=contact,
                service=service,
                money=money,
                client_from=client_from,
                client_status=client_status,
            )
            try: 
                session.add(client)
            except ProgrammingError as e:
                pass
    return client.client_id

async def get_all_clients(session_maker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(Client))
            clients = result.scalars().all()
            return [client.as_dict() for client in clients]