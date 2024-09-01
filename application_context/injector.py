from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from injector import Module, Binder, singleton, provider, Injector
from services.user_service import UserService
from repositories.user_repository import UserRepository
from mappers.user_mapper import UserMapper
from flask import Flask

# Assuming the app config has been set up properly
def get_db_session(app: Flask):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    session_factory = sessionmaker(bind=engine)
    return scoped_session(session_factory)

class AppModule(Module):
    def configure(self, binder: Binder):
        binder.bind(UserRepository, to=UserRepository, scope=singleton)
        binder.bind(UserMapper, to=UserMapper, scope=singleton)
        binder.bind(UserService, to=UserService, scope=singleton)

    @singleton
    @provider
    def provide_db_session(self, app: Flask) -> scoped_session:
        return get_db_session(app)

def configure_injector(binder: Binder):
    binder.install(AppModule)
