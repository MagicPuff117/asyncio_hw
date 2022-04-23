import asyncio

from settings import user, password, host, port, db_name

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_async_engine(
        f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}',
        echo=True,
    )

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
    )


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    pers_id = Column(Integer)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(String)
    starships = Column(String)
    vehicles = Column(String)


async def async_create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(async_create_tables())