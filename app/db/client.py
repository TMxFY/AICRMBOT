from sqlalchemy.exc import ProgrammingError
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, select, BigInteger, DateTime  # type: ignore
from .base import Base   
from sqlalchemy.orm import sessionmaker
from redis.asyncio.client import Redis
from sqlalchemy.orm import relationship 
from sqlalchemy import select, func

class Client(Base):
    __tablename__ = 'client'
    client_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    contact = Column(VARCHAR(255), nullable=False)
    service = Column(VARCHAR(255), nullable=False) # сделать потом выпадающий список
    money = Column(Integer, nullable=False)
    client_from = Column(BigInteger, ForeignKey('client_from.from_id'), nullable=False)
    client_status = Column(BigInteger, ForeignKey('client_status.status_id'), nullable=False) # сделать потом выпадающий список
    date = Column(DateTime(timezone=True), default=func.now())

    client_status_rel = relationship('ClientStatus', foreign_keys=[client_status])
    client_from_rel = relationship('ClientFrom', foreign_keys=[client_from])

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class ClientStatus(Base):
    __tablename__ = 'client_status'
    status_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    status = Column(VARCHAR(255), nullable=False)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class ClientFrom(Base):
    __tablename__ = 'client_from'
    from_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    clientfrom = Column(VARCHAR(255), nullable=False)

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
        
async def count_all_clients(session_maker):
    async with session_maker() as session:
        async with session.begin():
            resultmoney = await session.execute(select(Client.money))
            clientmoneytotal = resultmoney.scalars().all()
            totalclient = await session.execute(select(Client.client_id))
            totalclient = totalclient.scalars().all()
            return [clientmoneytotal,totalclient]

async def get_all_status(session_maker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(ClientStatus))
            statuses = result.scalars().all()
            return [status.as_dict() for status in statuses]
        
async def get_all_froms(session_maker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(ClientFrom))
            froms = result.scalars().all()
            return [froma.as_dict() for froma in froms]