from flask import jsonify
from injector import inject
from app.services.user_service import UserService

class UserResource:
    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def register_routes(self, app, namespace):
        app.add_url_rule(f'{namespace}/<int:user_id>', view_func=self.get_user, methods=['GET'])
        # You can add more routes here, all under the same namespace

    def get_user(self, user_id):
        user = self.user_service.get_user(user_id)
        return user.json(), 200
