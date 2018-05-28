from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

def create_app():
    db.init_app(app)
    return app

from flask_migrate_demo import models