import sys
sys.path.insert(0, '../')
import unittest
from model.users.user_model import UserModel
from model.sql_helper import get_session


class TestUserModel(unittest.TestCase):

    def test_check_user_exist_by_name(self):
        self.assertTrue(UserModel().check_user_exist_by_name(**{"username": "asbccc3"}))
        self.assertFalse(UserModel().check_user_exist_by_name(**{"username": "asbccc2"}))

    def test_create_user(self):
        users = [
            {
                "name": "asbccc3",
                "email": "test@gmail.com",
                "password": "abc123"
            },
            {
                "name": "peterflin",
                "email": "peterflin@gmail.com",
                "password": "abc123"
            },
            {
                "name": "peterflin2",
                "email": "peterflin@gmail.com",
                "password": "abc123"
            }
        ]
        success_message = {"result": "success", "message": "user created"}
        fail_message = {"result": "fail", "message": "user already exist"}
        for user in users:
            result = UserModel().create_user(**user)
            self.created_id = result.pop('id')
            self.assertEqual(result, success_message)
        for user in users:
            result = UserModel().create_user(**user)
            self.assertEqual(result, fail_message)

    def test_delete_user(self):
        success_message = {"result": "success", "message": "user deleted"}
        fail_message = {"result": "fail", "message": "user not exist"}
        result = UserModel().delete_user(user_id=3)
        self.assertEqual(result, success_message)

        result = UserModel().delete_user(user_id=0)
        self.assertEqual(result, fail_message)

    def test_check_user_exist_by_id(self):
        self.assertTrue(UserModel().check_user_exist_by_id(user_id=1))
        self.assertTrue(UserModel().check_user_exist_by_id(user_id=2))
        self.assertFalse(UserModel().check_user_exist_by_id(user_id=3))

    def test_get_password(self):
        # 給予username並回傳password
        self.assertEqual(type(UserModel().get_password(username="asbccc3")), str)
        self.assertEqual(len(UserModel().get_password(username="asbccc3")), 60)
        # self.assertEqual(UserModel().get_password(username="peterflin"), "$2b$12$kKob3hRIORYO.7rSud0Xnu84QEo2BqiT7AhDJ.kgxLyyPMDxcJBjC")
        with self.assertRaises(ValueError):
            UserModel().get_password(username="test123")

    def test_update_user_info(self):
        update_info = {
            "name": "peterflin",
            "email": "peterflin123@gmail.com"
        }
        success_message = {"result": "success", "message": "user info updated"}
        fail_message = {"result": "fail", "message": "user not exist"}
        self.assertEqual(UserModel().update_user_info(user_id=2, **update_info), success_message)
        self.assertEqual(UserModel().update_user_info(user_id=0, **update_info), fail_message)


if __name__ == "__main__":
    # init script
    session = get_session("user")
    session.execute("TRUNCATE users")
    session.commit()
    session.close()
    # test script
    suite = unittest.TestSuite()
    suite.addTest(TestUserModel('test_create_user'))
    suite.addTest(TestUserModel('test_delete_user'))
    suite.addTest(TestUserModel('test_get_password'))
    suite.addTest(TestUserModel('test_check_user_exist_by_id'))
    suite.addTest(TestUserModel('test_check_user_exist_by_name'))
    suite.addTest(TestUserModel('test_update_user_info'))
    unittest.TextTestRunner(verbosity=2).run(suite)
