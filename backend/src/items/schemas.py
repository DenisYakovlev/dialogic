from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float

    class Config:
        from_attributes = True


class ItemCreate(ItemBase):
    pass


class ItemFull(ItemBase):
    id: int