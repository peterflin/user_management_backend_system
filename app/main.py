# 我想寫一個具有登入系統的Web API
# 並且可以記錄登入紀錄

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers.users.users_controller import users_router
import sqlalchemy


app = FastAPI()
app.include_router(users_router)


@app.get("/healthy_check", include_in_schema=False)
async def root():
    return {"Healthy": "True"}


@app.exception_handler(sqlalchemy.exc.OperationalError)
async def mysql_operation_exception_handler(request: Request, exc: sqlalchemy.exc.OperationalError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"detail": "Database connection failed"}),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )
