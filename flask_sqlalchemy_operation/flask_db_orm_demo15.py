from flask import Flask
from sqlalchemy import Column, String, Integer, ForeignKey, Enum, func
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, backref, relationship

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
Base = declarative_base(engine)
session = sessionmaker(engine)()


@app.route('/')
def index():
    return 'hello world'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', backref='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.title)

Base.metadata.drop_all()
Base.metadata.create_all()

u1 = User(name='zhangsan')
u2 = User(name='lisi')

for i in range(1):
    p = Post(title='post%s' % i)
    p.author = u1
    session.add(p)
session.commit()

for i in range(1, 3):
    p = Post(title='post%s' % i)
    p.author = u2
    session.add(p)
session.commit()

"""
sql 语句:

mysql> select * from user join post on user.id = post.user_id;
+----+----------+----+-------+---------+
| id | name     | id | title | user_id |
+----+----------+----+-------+---------+
|  1 | zhangsan |  1 | post0 |       1 |
|  2 | lisi     |  2 | post1 |       2 |
|  2 | lisi     |  3 | post2 |       2 |
+----+----------+----+-------+---------+
3 rows in set (0.01 sec)

mysql> select user.name, count(user.id) from user join post on user.id = post.user_id group by user.id;
+----------+----------------+
| name     | count(user.id) |
+----------+----------------+
| zhangsan |              1 |
| lisi     |              2 |
+----------+----------------+
2 rows in set (0.00 sec)

mysql> select user.name, count(user.id) from user join post on user.id = post.user_id group by user.id order by count(user.id) desc;
+----------+----------------+
| name     | count(user.id) |
+----------+----------------+
| lisi     |              2 |
| zhangsan |              1 |
+----------+----------------+
2 rows in set (0.00 sec)
"""
# 找到所有用户, 按照发表的文章进行降序排序
result = session.query(User.name, func.count(User.id)).join(Post, User.id == Post.user_id)\
                            .group_by(User.id).order_by(func.count(Post.id).desc()).all()
print(result) # [('lisi', 2), ('zhangsan', 1)]