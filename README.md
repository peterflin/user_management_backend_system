# FastAPI 使用者管理API

## 專案描述
使⽤ FastAPI 和 SQLAlchemy 創建⼀個簡單的使⽤者資料庫管理 RESTful API，並使用MVC概念進行程式設計 
提供以下功能:
1. 創建使用者
2. 登入取得JWT
3. 透過ID檢索使用者(須帶入JWT)
4. 更新使用者資訊(須帶入JWT)
5. 刪除使用者(須帶入JWT)

## Tech Stack
- Python 3.9.13
- FastAPI
- SQLAlchemy
- MySQL

## 運行專案
```bash
cd app
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoint

- [/users/login](#userslogin) : 登入取得JWT
- [/users/get_user_info](#usersget_user_info) : 透過ID檢索使用者(須帶入JWT)
- [/users/create_user](#userscreate_user) : 創建使用者
- [/users/update_user_info](#usersupdate_user_info) : 更新使用者資訊(須帶入JWT)
- [/users/delete_user](#usersdelete_user) : 刪除使用者(須帶入JWT)

## SQLAlchemy表格
請參考`model/users/orm_model.py`

## Database
- MySQL

### Schema
- Databbase: user_management
    - Table: users

### DB導入

#### 導入有資料的Table
```bash
mysql -u username -p database_name < user_management_with_data.sql
```

#### 只導入Table Schema
```bash
mysql -u username -p database_name < user_management.sql
```

#### Docker啟動MySQL
```bash
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0-bullseye
```

## 測試
請參考`test/README.md`
