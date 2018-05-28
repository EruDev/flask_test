from flask_migrate_demo import db

class BackendUser(db.Model):
    __tablename__ = 'backend_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<BackendUser {}>'.format(self.username)

db.create_all()