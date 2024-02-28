from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from routers.users.model import User, UserCreateResult, UserUpdate
from model.users.user_model import UserModel
from utils.jwt_verify import verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, TokenData, get_current_active_user
from datetime import timedelta


users_router = APIRouter()


@users_router.post("/users/create_user", tags=["User"], response_model=UserCreateResult)
def create_user(user_info: User):
    # return UserModel().create_user(**user_info.model_dump())
    return UserModel().create_user(name=user_info.name, password=user_info.password, email=user_info.email)


@users_router.get("/users/get_user_info", tags=["User"])
def get_user(user_id: int, current_user: User = Depends(get_current_active_user)):
    return UserModel().get_user_info_by_id(user_id)


@users_router.put("/users/update_user_info", tags=["User"])
def update_user_info(user_info: UserUpdate, current_user: User = Depends(get_current_active_user)):
    return UserModel().update_user_info(**user_info.model_dump())


@users_router.delete("/users/delete_user", tags=["User"])
def delete_user(user_id: int, current_user: User = Depends(get_current_active_user)):
    return UserModel().delete_user(user_id)


@users_router.post("/users/login", tags=["User"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_password = UserModel().get_password(form_data.username)
    user = verify_password(form_data.password, user_password)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": access_token, "token_type": "bearer"}
