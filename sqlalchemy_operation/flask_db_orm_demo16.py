from flask import Flask
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


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
Base = declarative_base(engine)
session = sessionmaker(engine)()


@app.route('/')
def index():
    return 'hello world'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    city = Column(String(128), nullable=False)
    age = Column(Integer, default=0)

    def __repr__(self):
        return '<User {}>'.format(self.name)

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# u1 = User(name='张三', city='北京', age=22)
# u2 = User(name='李四', city='北京', age=22)
# u3 = User(name='王五', city='北京', age=22)
# u4 = User(name='马六', city='深圳', age=20)
#
# session.add_all([u1, u2, u3, u4])
# session.commit()


# user = session.query(User).filter(User.name == '张三').first()
# print(user)
# users = session.query(User).filter(User.city == user.city).all()
# print(users)

# 子查询, 查询出和张三年龄相仿并且在同一个城市的人  label 相当于起别名 as
user = session.query(User.city.label("city"), User.age.label("age")).filter(User.name == '张三').subquery()
# print(user)
users = session.query(User).filter(User.city == user.c.city, User.age == user.c.age).all()
print(users)

"""
原生 sql语句

SELECT user.id AS user_id, user.name AS user_name, user.city AS user_city, user.age AS user_age 
FROM user, (SELECT user.city AS city, user.age AS age 
FROM user 
WHERE user.name = %(name_1)s) AS anon_1 
WHERE user.city = anon_1.city AND user.age = anon_1.age
"""