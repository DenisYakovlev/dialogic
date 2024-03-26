from sqlalchemy import Column, Float, Integer, String

from src.db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=True)
    description = Column(String(length=1024), unique=False, nullable=True)
    price = Column(Float, unique=False, nullable=True)
