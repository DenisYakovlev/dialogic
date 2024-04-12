from typing import Annotated, List
from fastapi import APIRouter, Depends
from src.dependencies import get_main_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.users.models import User
from src.users.schemas import UserSchema, UserCreateSchema
from src.users import services


router = APIRouter(prefix="/users")


@router.get("/")
async def list_users(db: Annotated[AsyncSession, Depends(get_main_db)]):
    """
    List all users from db
    """
    users: List[User] = await services.list_users(db)

    return users


@router.post("/", response_model=UserSchema)
async def create_user(user: UserCreateSchema, db: Annotated[AsyncSession, Depends(get_main_db)]):
    new_user: User = await services.create_user(user, db) 

    return new_user