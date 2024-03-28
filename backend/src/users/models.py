from sqlalchemy import Boolean, Column, DateTime, Integer, String, func

from src.config import settings
from src.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=True)
    is_active = Column(Boolean, default=False)
    role = Column(String, unique=False, nullable=False, server_default=settings.DEFAULT_PERMISSION_ROLE)
    created_at = Column(DateTime, server_default=func.now())
