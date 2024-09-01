from app.models.user import User
from sqlalchemy.orm import scoped_session
from injector import inject

class UserRepository:
    @inject
    def __init__(self, db_session: scoped_session):
        self.db_session = db_session

    def get_by_id(self, user_id):
        return self.db_session.query(User).filter_by(id=user_id).first()
