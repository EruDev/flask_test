from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'hello world'

class BackendUser(db.Model):
    __tablename__ = 'backend_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<BackendUser {}>'.format(self.username)


db.drop_all()
db.create_all()


