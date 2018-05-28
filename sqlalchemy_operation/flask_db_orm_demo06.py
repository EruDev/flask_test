from datetime import datetime
from flask import Flask
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = '127.0.0.1'
DB = 'flask_sqlalchemy01'
USER = 'root'
PASSWORD = 'your password'
PORT = 3306

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})

# mysql+pymysql://root:root@127.0.0.1:3306/flask_sqlalchemy01?charset=utf8
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
    name = Column(String(64), nullable=False)
    age = Column(Integer)
    is_delete = Column(Boolean, default=False)
    create_time = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='NO ACTION')) # ondelete=('CASCADE'级联操作, 'SET NULL', 'RESTRICT','NO ACTION')

    def __repr__(self):
        return '<Post {}>'.format(self.title)

Base.metadata.drop_all()
Base.metadata.create_all()

u = User(name='zhangsan', age=18)
session.add(u)
session.commit()
p = Post(title='post01', user_id=1)
session.add(p)
session.commit()
