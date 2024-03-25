from db import Base
from sqlalchemy import Column, String, Integer, Float


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=True)
    price = Column(Float, unique=False, nullable=True)