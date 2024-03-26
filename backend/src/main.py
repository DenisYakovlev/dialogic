from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import settings
from src.db import main_sessionmanager, store_sessionmanager
from src.items.router import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init db connections
    main_sessionmanager.init(host=settings.DATABASES.get("main").DB_URL)
    store_sessionmanager.init(host=settings.DATABASES.get("store").DB_URL)

    yield

    # close db sessions
    await main_sessionmanager.close()
    await store_sessionmanager.close()


app = FastAPI(lifespan=lifespan)

app.include_router(items_router)
