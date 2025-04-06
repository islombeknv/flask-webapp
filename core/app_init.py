import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from core.models import Base


db = SQLAlchemy(model_class=Base)

def create_app(routes):
    static = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
    
    app = Flask(__name__, static_folder=static)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(routes.bp)

    return app
