# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
