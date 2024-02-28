# 我想寫一個具有登入系統的Web API
# 並且可以記錄登入紀錄

from fastapi import FastAPI
from routers.users.users_controller import users_router


app = FastAPI()
app.include_router(users_router)


@app.get("/healthy_check", include_in_schema=False)
async def root():
    return {"Healthy": "True"}
