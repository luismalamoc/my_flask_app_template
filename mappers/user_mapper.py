from models.user import User
from schemas.user_schema import UserSchema

class UserMapper:
    def to_schema(self, user: User) -> UserSchema:
        return UserSchema(
            id=user.id,
            name=user.name,
            email=user.email
        )
