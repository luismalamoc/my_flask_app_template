import pytest
from app.services.user_service import UserService
from app.models.user import User
from app.mappers.user_mapper import UserMapper

@pytest.fixture
def mock_user_repository(mocker):
    return mocker.Mock()

@pytest.fixture
def mock_user_mapper(mocker):
    return mocker.Mock(spec=UserMapper)

@pytest.fixture
def user_service(mock_user_repository, mock_user_mapper):
    return UserService(mock_user_repository, mock_user_mapper)

def test_get_user(user_service, mock_user_repository, mock_user_mapper):
    mock_user = User(id=1, name="John Doe", email="john.doe@example.com")
    mock_user_repository.get_by_id.return_value = mock_user

    user_schema = user_service.get_user(1)

    mock_user_repository.get_by_id.assert_called_once_with(1)
    mock_user_mapper.to_schema.assert_called_once_with(mock_user)
