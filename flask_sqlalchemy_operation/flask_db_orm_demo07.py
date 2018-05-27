from flask import Flask
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'your password'
DB = 'flask_sqlalchemy01'
PORT = 3306

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True # 自动加载模板, 意思是如果代码有改动 不需要重启服务器
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
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(64))
    age = Column(Integer)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(Text, default=None)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE')) # 级联操作
    # author 可以通过 post.author 查询到发表这篇文章的作者
    author = relationship('User', backref='articles') # backref 反向引用, user.articles 可以直接查询到该用户发表的文章

    def __repr__(self):
        return '<Post {}>'.format(self.title)


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# u = User(name='zhangsan', age=18)
# session.add(u)
# session.commit()
#
# for i in range(6):
#     post = Post(title='post%s' % i, user_id=1)
#     session.add(post)
# session.commit()

# post = session.query(Post).first()
# print(post)
# user = session.query(User).get(post.user_id)
# print(user)
# post = session.query(Post).first()
# print(post.author.age)
user = session.query(User).get(1)
print(user.articles)