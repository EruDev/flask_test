from flask import Flask
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, backref, relationship

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'your password'
DB = 'flask_sqlalchemy01'
PORT = 3306

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'\
                            .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


@app.route('/')
def index():
    return 'hello world'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=Flask)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', backref=backref('posts', lazy='dynamic'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# u = User(name='zhangsan')
# for i in range(100):
#     p = Post(title='post %s' % i)
#     p.author = u
#     session.add(u)
# session.commit()
p = Post(title='test101')
u = session.query(User).first()
u.posts.append(p)
session.commit()
