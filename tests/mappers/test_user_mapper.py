from app.mappers.user_mapper import UserMapper
from app.models.user import User
from app.schemas.user_schema import UserSchema

def test_to_schema():
    user = User(id=1, name="John Doe", email="john.doe@example.com")
    mapper = UserMapper()

    user_schema = mapper.to_schema(user)

    assert isinstance(user_schema, UserSchema)
    assert user_schema.id == user.id
    assert user_schema.name == user.name
    assert user_schema.email == user.email
