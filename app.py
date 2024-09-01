from flask import Flask
from injector import Injector
from config import development
from application_context.injector import configure_injector, get_db_session
from resources.user_resource import UserResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(development)

    injector = Injector([configure_injector])

    # Set up the db session
    db_session = injector.get(scoped_session)

    with app.app_context():
        injector.get(UserResource).register_routes(app, '/users')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
