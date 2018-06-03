from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    deposit = db.Column(db.Float, nullable=False, default=0)

    def __repr__(self):
        return '<User> {}'.format(self.username)
