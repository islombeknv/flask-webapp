# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("AZURE_SQL_CONNECTION_STRING")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
