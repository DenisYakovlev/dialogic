import os
from enum import Enum
from typing import Dict, List

import pytz
from datetime import tzinfo
from dotenv import load_dotenv
from pydantic import BaseModel, computed_field
from pydantic_settings import BaseSettings

load_dotenv()


class DBConfig(BaseModel):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str

    @computed_field
    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"
    

class PermissionRoles(str, Enum):
    user = "user"
    admin = "admin"
    any = "any"


class Settings(BaseSettings):
    APP_NAME: str = "smart tables api"

    DATABASES: Dict[str, DBConfig] = {
        "main": DBConfig(
            DB_USER=os.getenv("MAIN_DB_USER"),
            DB_PASSWORD=os.getenv("MAIN_DB_PASSWORD"),
            DB_HOST=os.getenv("MAIN_DB_HOST"),
            DB_NAME=os.getenv("MAIN_DB_NAME")
        ),
        "store": DBConfig(
            DB_USER=os.getenv("STORE_DB_USER"),
            DB_PASSWORD=os.getenv("STORE_DB_PASSWORD"),
            DB_HOST=os.getenv("STORE_DB_HOST"),
            DB_NAME=os.getenv("STORE_DB_NAME")
        )
    }

    DEFAULT_PERMISSION_ROLE: str = PermissionRoles.user.value

    TIMEZONE: str = "UTC"
    PYTZ_TZ: tzinfo = pytz.timezone(zone=TIMEZONE)


settings = Settings()
