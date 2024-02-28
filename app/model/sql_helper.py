from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# engine會使用mysql+pymysql來進行登入
db_engine = {
    "user": create_engine('mysql+pymysql://root:@localhost:3306/user_management'),
}


# 建立session
def get_session(role):
    if role not in db_engine:
        raise ValueError("Invalid role")
    Session = sessionmaker(bind=db_engine[role])
    session = Session()
    return session
