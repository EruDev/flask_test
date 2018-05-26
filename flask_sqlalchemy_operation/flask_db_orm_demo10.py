from flask import Flask
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
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
session = sessionmaker(engine)()
Base = declarative_base(engine)


@app.route('/')
def index():
    return 'hello world'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    posts = relationship('Post', backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', backref='posts', cascade='save-update, delete') # save-update 是默认选项 delete如果文章被删除了, 那么文章也会相应的作者跟着被删除 也就是级联操作

    def __repr__(self):
        return '<Post {}>'.format(self.title)

def init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    u = User(name='zhangsan')
    p = Post(title='post01')
    p.author = u
    # session.add(u)
    session.add(p)
    session.commit()

def opertion():
    p = session.query(Post).first()
    session.delete(p)
    session.commit()


if __name__ == '__main__':
    # init_db()
    opertion()