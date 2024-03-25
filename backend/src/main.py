from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import settings
from db import sessionmanager
from items.router import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init db host
    sessionmanager.init(host=settings.DB_URL)

    yield

    # close db session
    await sessionmanager.close()


app = FastAPI(lifespan=lifespan)

app.include_router(items_router)
