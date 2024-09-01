import pytest
from flask import Flask
from app.resources.user_resource import UserResource
from app.services.user_service import UserService
from app.schemas.user_schema import UserSchema

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

@pytest.fixture
def mock_user_service(mocker):
    return mocker.Mock(spec=UserService)

@pytest.fixture
def user_resource(mock_user_service):
    return UserResource(mock_user_service)

def test_get_user(app, user_resource, mock_user_service, mocker):
    # Mock the UserSchema and its json() method
    mock_user = mocker.Mock(spec=UserSchema)
    mock_user.json.return_value = {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    # Mock the user_service.get_user to return the mock_user
    mock_user_service.get_user.return_value = mock_user

    with app.test_request_context():
        response = user_resource.get_user(1)
        json_data = response[0]

    assert response[1] == 200
    assert json_data['id'] == 1
    assert json_data['name'] == "John Doe"
    assert json_data['email'] == "john.doe@example.com"
    mock_user_service.get_user.assert_called_once_with(1)
    mock_user.json.assert_called_once()
