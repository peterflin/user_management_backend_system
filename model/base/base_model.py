from model.sql_helper import get_session


class BaseSQLModel:

    def __init__(self, role):
        self.session = get_session(role)

    def __del__(self):
        self.session.close()
