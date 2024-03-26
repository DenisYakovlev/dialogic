from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]

    class Config:
        from_attributes = True


class ItemCreate(ItemBase):
    pass


class ItemFull(ItemBase):
    id: int