from datetime import datetime
from typing import Annotated
from typing_extensions import Self
from pydantic import BaseModel, EmailStr, model_validator, Field
from src.users.exceptions import PasswordsDoNotMatchError


class BaseUserSchema(BaseModel):
    email: EmailStr


class UserSchema(BaseUserSchema):
    id: int
    is_active: bool
    role: str
    created_at: datetime


class UserCreateSchema(BaseUserSchema):
    password: str = Field(min_length=8, pattern=r'^[0-9a-zA-Z_]{8,}$')
    re_password: str = Field(min_length=8, pattern=r'^[0-9a-zA-Z_]{8,}$')
    
    @model_validator(mode="after")
    def check_password_match(self) -> Self:
        if self.password != self.re_password:
            raise PasswordsDoNotMatchError("Passwords do not match")
        
        return self