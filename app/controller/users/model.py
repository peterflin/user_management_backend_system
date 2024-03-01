from pydantic import BaseModel, Field
from typing import Union


class User(BaseModel):
    name: str
    email: Union[str, None]
    password: str


class CreateUser(BaseModel):
    name: str = Field(max_length=20, pattern=r'^[a-zA-Z0-9]+$')
    email: Union[str, None] = Field(pattern=r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    password: str = Field(max_length=20, pattern=r'^[a-zA-Z0-9@_]+$')


class UserCreateSuccess(BaseModel):
    result: str
    message: str
    id: int


class UserCreateFail(BaseModel):
    result: str
    message: str


class UserUpdate(BaseModel):
    user_id: int
    name: str = Field(max_length=20, pattern=r'^[a-zA-Z0-9]+$')
    email: str = Field(pattern=r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


class UserUpdateOut(BaseModel):
    id: int
