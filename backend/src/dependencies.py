from src.db import main_sessionmanager, store_sessionmanager


async def get_main_db():
    async with main_sessionmanager.session() as session:
        yield session


async def get_store_db():
    async with store_sessionmanager.session() as session:
        yield session
