from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Union
from controller.users.model import User, CreateUser, UserCreateSuccess, UserCreateFail, UserUpdate
from controller.users.users_controller import UsersController
from utils.jwt_verify import get_current_active_user
from fastapi import HTTPException


users_router = APIRouter()


@users_router.post(
    "/users/create_user",
    tags=["User"],
    response_model=Union[UserCreateSuccess, UserCreateFail]
)
def create_user(user_info: CreateUser):
    return UsersController().create_user(user_info)


@users_router.get("/users/get_user_info", tags=["User"])
def get_user(user_id: int, current_user: User = Depends(get_current_active_user)):
    return UsersController().get_user_info(user_id, current_user)


@users_router.put("/users/update_user_info", tags=["User"])
def update_user_info(user_info: UserUpdate, current_user: User = Depends(get_current_active_user)):
    return UsersController().update_user_info(user_info, current_user)


@users_router.delete("/users/delete_user", tags=["User"])
def delete_user(user_id: int, current_user: User = Depends(get_current_active_user)):
    return UsersController().delete_user(user_id, current_user)


@users_router.post("/users/login", tags=["User"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return UsersController().login_for_access_token(form_data)
