from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from src.users.models import User
from src.users.schemas import UserCreateSchema
from src.users.exceptions import EmailIsTakenError
from fastapi import HTTPException


async def list_users(db: AsyncSession) -> List[User]:
    query = select(User)
    result = await db.execute(query)

    users: List[User] = result.scalars().all()
    return users


async def create_user(user: UserCreateSchema, db: AsyncSession) -> User:
    new_user = User(
        email=user.email,
        password=user.password
    )

    new_user.hash_password()
    
    db.add(new_user)

    try:
        await db.commit()
        await db.refresh(new_user)
    except IntegrityError:
        raise EmailIsTakenError()

    return new_user