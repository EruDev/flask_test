from random import randint
from flask import Flask
from sqlalchemy import create_engine, Column, String, Integer, Text, or_
from sqlalchemy.ext.declarative import declarative_base # 创建数据库模型对象的基类
from sqlalchemy.orm import sessionmaker  # session 用于对数据库的交互操作


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'


HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'your password'
DB = 'flask_sqlalchemy01'
PORT = 3306

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'\
                                .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)  # 创建模型对象的基类
session = sessionmaker(engine)()


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)
    price = Column(Integer)
    content = Column(Text, default=None)

    def __repr__(self):
        return '<Post {}>'.format(self.title)


# Base.metadata.drop_all()
# Base.metadata.create_all()

# for i in range(6):
#     post = Post(title='test %s' % i, price=randint(1, 100))
#     session.add(post)
# session.commit()

# posts = session.query(Post).all()
# print(posts)

# post = session.query(Post).filter(Post.title != 'test 0').first()
# print(post)

# like & ilike(不区分大小写)

# post = session.query(Post).filter(Post.title.ilike('Test%')).all()
# print(post)

# not in & in ~ 表示取反
# post = session.query(Post).filter(~Post.title.in_(['test 0', 'test 1'])).all()
# print(post)

# is null & is not null
# post = session.query(Post).filter(Post.content != None).all()
# print(post)

# or
post = session.query(Post).filter(or_(Post.title == 'bbb', Post.content == 'aaa')).all()
print(post)