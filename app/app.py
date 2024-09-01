import os

from flask import Flask
from injector import Injector
from app.config import development, testing
from app.config import production
from app.application_context import configure_injector
from app.resources import UserResource
from sqlalchemy.orm import scoped_session
from app.models import Base  # Import your base model class

def create_app():
    app = Flask(__name__)
    # Load the appropriate config based on the FLASK_ENV environment variable
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(production)
    elif env == 'testing':
        app.config.from_object(testing)
    else:
        app.config.from_object(development)

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
