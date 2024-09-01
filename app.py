from flask import Flask
from injector import Injector, singleton, Binder
from config import app_config
from application_context.injector import configure_injector
from resources.user_resource import UserResource
from sqlalchemy.orm import scoped_session
from models import Base  # Import your base model class

def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config)

    # Manually create the Injector and configure it
    injector = Injector([configure_injector])

    with app.app_context():
        # Set up the db session
        db_session = injector.get(scoped_session)

        # Create all tables in the database
        engine = db_session.bind
        Base.metadata.create_all(engine)

        # Register routes
        user_resource = injector.get(UserResource)
        user_resource.register_routes(app, '/users')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
