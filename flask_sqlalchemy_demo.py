from flask import Flask
from flask_sqlalchemy import SQLAlchemy


HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
DB = 'flask_sqlalchemy_demo'
PORT = 3306

app = Flask(__name__)

# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'\
                            .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)

# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True,
    'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
})
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'hello world'


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    # lazy='dynamic' 'dynamic' loaders cannot be used with many-to-one/one-to-one relationships and/or uselist=False.
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)


if __name__ == '__main__':
    # app.run()
    # db.drop_all()
    # db.create_all()
    # u = User(name='zhangsan')
    # p = Post(title='post01')
    # p.author = u
    # db.session.add(u)
    # db.session.commit()
    # user = User.query.all()
    # print(user)
    # u = User(name='aaa')
    # p = Post(title='post02')
    # p.author = u
    # db.session.add(u)
    # db.session.commit()
    # print(User.query.order_by(User.name.desc()).all())
    import os
    file_path = os.path.abspath(__file__)
    file_dirname = os.path.dirname(__file__)
    print(file_path) # 获取当前文件的所在路径
    print(file_dirname) # 获取当前文件的所在目录