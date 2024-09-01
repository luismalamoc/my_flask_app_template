import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///dev.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
