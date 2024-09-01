from app.repositories.user_repository import UserRepository
from app.mappers.user_mapper import UserMapper
from injector import inject

class UserService:
    @inject
    def __init__(self, user_repository: UserRepository, user_mapper: UserMapper):
        self.user_repository = user_repository
        self.user_mapper = user_mapper

    def get_user(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        return self.user_mapper.to_schema(user)
