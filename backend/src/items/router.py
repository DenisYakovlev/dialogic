from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from src.db import get_main_db
from src.items.models import Item
from src.items.schemas import ItemFull, ItemCreate


router = APIRouter(prefix="/items")


@router.get("", response_model=List[ItemFull])
async def list_items(db: AsyncSession = Depends(get_main_db)):
    items = (await db.execute(select(Item))).scalars().all()
    return items


@router.post("", response_model=ItemFull)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_main_db)):
    new_item = Item(**item.model_dump())

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item
