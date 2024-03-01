from functools import wraps
from sqlalchemy.exc import OperationalError
from fastapi import HTTPException, status


def handle_operational_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database connection failed"
            )
    return wrapper
