from datetime import datetime
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import EmailStr

from src.config import settings, PermissionRoles
from src.users.exceptions import PasswordIsEmptyError
from src.db import Base
import bcrypt


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[EmailStr] = mapped_column(String(320), unique=True)
    password: Mapped[str] 
    role: Mapped[PermissionRoles] = mapped_column(default=settings.DEFAULT_PERMISSION_ROLE)

    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())


    def hash_password(self) -> None:
        if self.password is None:
            raise PasswordIsEmptyError("Password can't be None")
        
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode("utf-8"), salt)

        self.password = hashed_password.decode("utf-8")
