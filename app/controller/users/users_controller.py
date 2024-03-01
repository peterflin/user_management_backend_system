from fastapi import HTTPException, status
from datetime import timedelta
from controller.users.model import User, UserUpdate
from model.users.user_model import UserModel
from utils.jwt_verify import verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token


class UsersController:

    def create_user(self, user_info: User):
        result = UserModel().create_user(name=user_info.name, password=user_info.password, email=user_info.email)
        if result["result"] == "fail":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["message"])
        return result

    def get_user_info(self, user_id: int, current_user):
        result = UserModel().get_user_info_by_id(user_id)
        if result["result"] == "fail":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["data"])
        return result

    def update_user_info(self, user_info: UserUpdate, current_user):
        return UserModel().update_user_info(**user_info.model_dump())

    def delete_user(self, user_id: int, current_user):
        result = UserModel().delete_user(user_id)
        if result["result"] == "fail":
            raise HTTPException(status_code=400, detail=result["message"])
        return result

    def login_for_access_token(self, form_data):
        user_data = UserModel().get_password(form_data.username)
        user = verify_password(form_data.password, user_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": form_data.username, "id": user_data.id}, expires_delta=access_token_expires
        )
        if not access_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"access_token": access_token, "token_type": "bearer"}
