# 測試

## API測項目錄

- [/users/login](#userslogin)
- [/users/get_user_info](#usersget_user_info)
- [/users/create_user](#userscreate_user)
- [/users/update_user_info](#usersupdate_user_info)
- [/users/delete_user](#usersdelete_user)

## 進行API測試
```bash
cd test/api_test
pytest
```

### 測項詳細

#### /users/login

- **`test_user_login_should_success`**: 正確輸入，預期成功登入。
- **`test_user_login_should_fail`**: 密碼輸入錯誤，預期登入失敗。

#### /users/get_user_info

- **`test_get_user_info_should_success`**: 正確登入取得 token，並成功取得已登入使用者的資訊。
- **`test_get_user_info_should_fail_by_get_an_not_exist_user`**: 正確登入取得 token，嘗試取得不存在的使用者 ID 的資訊，預期取得失敗。

#### /users/create_user

- **`test_create_user_should_success`**: 正確輸入，預期創建成功。
- **`test_create_user_should_fail_by_exist_user`**: 輸入已存在的使用者名稱，預期創建失敗。
- **`test_create_user_should_fail_by_name_string_too_long`**: 使用者名稱過長，預期創建失敗。
- **`test_create_user_should_fail_by_name_contains_space`**: 使用者名稱包含空白，預期創建失敗。
- **`test_create_user_should_fail_by_name_is_empty_string`**: 使用者名稱為空字串，預期創建失敗。
- **`test_create_user_should_fail_by_name_contains_special_character`**: 使用者名稱包含特殊字元，預期創建失敗。
- **`test_create_user_should_fail_by_password_string_too_long`**: 密碼過長，預期創建失敗。
- **`test_create_user_should_fail_by_password_is_empty_string`**: 密碼為空字串，預期創建失敗。
- **`test_create_user_should_fail_by_email_validation_fail`**: email 格式不正確，預期創建失敗。
- **`test_create_user_should_fail_by_email_is_empty_string`**: email 為空字串，預期創建失敗。

#### /users/update_user_info

- **`test_update_user_info_should_success`**: 正確登入後，輸入正確資料進行資料修改，預期修改成功。
- **`test_update_user_info_should_fail_by_name_format_validation_fail`**: 正確登入後，使用者名稱包含特殊字元，預期修改失敗。
- **`test_update_user_info_should_fail_by_email_format_validation_fail`**: 正確登入後，email 格式不正確，預期修改失敗。

#### /users/delete_user

- **`test_delete_user_should_success`**: 正確登入後，輸入正確資料進行使用者刪除，預期刪除成功。
- **`test_delete_user_should_fail`**: 正確登入後，指定不存在的使用者 ID，預期刪除失敗。


## 單元測試

使用unittest框架進行單元測試的撰寫

### 進行單元測試
```
cd test
python unit_test.py
```
