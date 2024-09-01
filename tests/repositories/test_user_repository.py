import pytest
from sqlalchemy.orm import scoped_session
from app.repositories.user_repository import UserRepository
from app.models.user import User


@pytest.fixture
def mock_db_session(mocker):
    # Mock the session object
    mock_session = mocker.Mock(spec=scoped_session)

    # Mock the query return object
    mock_query = mocker.Mock()
    mock_session.query.return_value = mock_query

    # Mock the filter_by return object
    mock_query.filter_by.return_value = mock_query

    # Mock the first method to return a mock user
    mock_user = User(id=1, name="John Doe", email="john.doe@example.com")
    mock_query.first.return_value = mock_user

    return mock_session


@pytest.fixture
def user_repository(mock_db_session):
    return UserRepository(mock_db_session)


def test_get_by_id(user_repository, mock_db_session):
    user = user_repository.get_by_id(1)

    # Check that the query, filter_by, and first methods were called correctly
    mock_db_session.query.assert_called_once_with(User)
    mock_db_session.query().filter_by.assert_called_once_with(id=1)
    mock_db_session.query().filter_by().first.assert_called_once()

    assert user.id == 1
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"
