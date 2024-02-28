from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    name: str
    email: Union[str, None]
    password: str


class UserCreateResult(BaseModel):
    result: str
    message: str
    id: Union[int, None]


class UserUpdate(BaseModel):
    user_id: int
    name: str
    email: str


class UserUpdateOut(BaseModel):
    id: int


class UserDelete(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_active: bool
