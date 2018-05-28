from datetime import datetime
from flask import Flask
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWORD = 'your password'
DB = 'flask_sqlalchemy01'

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

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64))
    create_time = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    author = relationship('User', backref=backref('posts', order_by=create_time.desc()))

    # __mapper_args__ = {
    #     'order_by': create_time.desc()
    # }

    def __repr__(self):
        return '<Post title:{} create_time: {}>'.format(self.title, self.create_time)


# Base.metadata.drop_all()
# Base.metadata.create_all()

# u = User(name='zhangsan')
# p1 = Post(title='post01', user_id=1)
# p2 = Post(title='post02', user_id=1)
# u.posts = [p1, p2]
# session.add(u)
# session.commit()

# p1 = Post(title='post01')
# p2 = Post(title='post02')
# session.add(p2)
# session.commit()
# p2 = Post(title='post02')
# posts = session.query(Post).order_by("-create_time").all()
# print(posts)
# posts = session.query(Post).all()
# print(posts)

# u = User(name='zhangsan')
# p = Post(title='title01')
# u.posts = [p]
# session.add(u)
# session.commit()
# import time
# time.sleep(2)
# p2 = Post(title='title02')
# u.posts.append(p2)
# # session.add(u)
# session.commit()

u = session.query(User).first()
print(u.posts)

