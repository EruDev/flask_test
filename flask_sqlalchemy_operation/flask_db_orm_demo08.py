from flask import Flask
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
PORT = 3306
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
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    extend = relationship('UserExtend', uselist=False) # 实现一对一关系

    def __repr__(self):
        return '<User {}>'.format(self.name)


class UserExtend(Base):
    __tablename__ = 'userextend'
    id = Column(Integer, autoincrement=True, primary_key=True)
    school = Column(String(128))
    user_id = Column(Integer, ForeignKey('user.id')) # 实现一对一关系

    user = relationship('User') # 实现一对一关系


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    title = Column(String(64), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))

    author = relationship('User', backref='articles')

    def __repr__(self):
        return '<User {}>'.format(self.title)


Base.metadata.drop_all()
Base.metadata.create_all()

# 一对一关系的实现
u = User(name='maliu', age=22)
school = UserExtend(school='beida')
u.extend = school
session.add(u)
session.commit()


# u = User(name='zhangsan', age=18)
# session.add(u)
# session.commit()
#
# for i in range(6):
#     p = Post(title='post%s' % i, user_id=1)
#     session.add(p)
# session.commit()

# u = session.query(User).get(1)
# print(u.articles)
# p = session.query(Post).get(1)
# print(p.author.name)

# p1 = Post(title='post01', user_id=1)
# p2 = Post(title='post02', user_id=1)
# u = session.query(User).get(1)
# u.articles.append(p1)
# u.articles.append(p2)
# session.add(u)
# session.commit()
