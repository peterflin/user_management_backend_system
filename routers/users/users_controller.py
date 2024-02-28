from fastapi import APIRouter, Request
from routers.users.model import User, UserCreateResult, UserUpdate
from model.users.user_model import UserModel


users_router = APIRouter()


@users_router.post("/users/create_user", tags=["User"], response_model=UserCreateResult)
def create_user(user_info: User):
    # return UserModel().create_user(**user_info.model_dump())
    return UserModel().create_user(name=user_info.name, password=user_info.password, email=user_info.email)


@users_router.get("/users/get_user_info", tags=["User"])
def get_user(user_id: int):
    return UserModel().get_user_info_by_id(user_id)


@users_router.put("/users/update_user_info", tags=["User"])
def update_user_info(user_info: UserUpdate):
    return UserModel().update_user_info(**user_info.model_dump())


@users_router.delete("/users/delete_user", tags=["User"])
def delete_user(user_id: int):
    return UserModel().delete_user(user_id)