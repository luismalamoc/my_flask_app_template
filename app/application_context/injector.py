from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from injector import Module, Binder, singleton, provider
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.mappers.user_mapper import UserMapper

# Create a database session factory
def get_db_session(database_uri: str):
    engine = create_engine(database_uri)
    session_factory = sessionmaker(bind=engine)
    return scoped_session(session_factory)

class AppModule(Module):
    def configure(self, binder: Binder):
        binder.bind(UserRepository, to=UserRepository, scope=singleton)
        binder.bind(UserMapper, to=UserMapper, scope=singleton)
        binder.bind(UserService, to=UserService, scope=singleton)

    @singleton
    @provider
    def provide_db_session(self) -> scoped_session:
        from flask import current_app
        return get_db_session(current_app.config['SQLALCHEMY_DATABASE_URI'])

def configure_injector(binder: Binder):
    binder.install(AppModule)
