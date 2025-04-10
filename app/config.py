import os
from dotenv import load_dotenv
load_dotenv()

""" Use this file to get the environment viriable it is much more safer and adds and extra level of abstraction on the sensitive data."""

DB_URL_POSTGRES = os.getenv("DB_URL_POSTGRES")
DB_URL_MONGODB = os.getenv("DB_URL_MONGODB")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
FRONT_URL = os.getenv("FRONT_URL")

