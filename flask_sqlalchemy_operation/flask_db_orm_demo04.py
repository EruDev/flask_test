from random import randint
from flask import Flask
from sqlalchemy import Column, String, Integer, Float, func
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = 'root'
PASSWORD = 'root'
PORT = 3306
HOST = '127.0.0.1'
DB = 'flask_sqlalchemy01'

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'\
                            .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(128), nullable=True)
    price = Column(Float)

    def __repr__(self):
        return '<Post {}>'.format(self.title)

# Base.metadata.drop_all()
# Base.metadata.create_all()

# for i in range(6):
#     post = Post(title='title %s' % i, price=randint(1, 10))
#     session.add(post)
# session.commit()

# posts = session.query(Post.title, Post.price).all()
# print(posts)

# 聚合函数
# result = session.query(func.count(Post.id)).first()
# print(result)
# result = session.query(func.min(Post.price)).first()
# print(result)
# result = session.query(func.max(Post.price)).first()
# print(result)
# result = session.query(func.sum(Post.price)).first()
# print(result)
result = session.query(func.avg(Post.price)).first()
print(result)