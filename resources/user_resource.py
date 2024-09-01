from flask import jsonify
from injector import inject
from services.user_service import UserService

class UserResource:
    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user(self, user_id):
        user = self.user_service.get_user(user_id)
        return jsonify(user), 200
