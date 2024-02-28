from model.base.base_model import BaseSQLModel
from model.users.orm_model import ORMUser


class UserModel(BaseSQLModel):

    def __init__(self) -> None:
        super().__init__("user")

    def create_user(self, name: str, password: str, email: str) -> None:
        if not self.check_user_exist_by_name(name):
            return {"result": "fail", "message": "user already exist"}
        user = ORMUser(name=name, email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return {
            "result": "success",
            "message": "user created",
            "id": self.get_user_id(name),
        }

    def check_user_exist_by_name(self, username: str) -> bool:
        user = self.session.query(ORMUser).filter(ORMUser.name == username).first()
        return user is None

    def check_user_exist_by_id(self, user_id: str) -> bool:
        user = self.session.query(ORMUser).filter(ORMUser.id == user_id).first()
        return user is None

    def get_user_id(self, username: str) -> int:
        user = self.session.query(ORMUser.id).filter(ORMUser.name == username).first()
        return user.id

    def get_user_info_by_id(self, user_id: int) -> dict:
        user = self.session.query(ORMUser.id, ORMUser.name, ORMUser.email).filter(ORMUser.id == user_id).first()
        return {"result": "success", "data": dict(user)}

    def update_user_info(self, user_id: int, name: str, email: str) -> dict:
        if not self.check_user_exist_by_id(user_id):
            return {"result": "fail", "message": "user not exist"}
        user = self.session.query(ORMUser).filter(ORMUser.id == user_id).first()
        user.name = name
        user.email = email
        self.session.commit()
        return {"result": "success", "message": "user info updated"}

    def delete_user(self, user_id: int) -> dict:
        if not self.check_user_exist_by_id(user_id):
            return {"result": "fail", "message": "user not exist"}
        user = self.session.query(ORMUser).filter(ORMUser.id == user_id).first()
        self.session.delete(user)
        self.session.commit()
        return {"result": "success", "message": "user deleted"}
