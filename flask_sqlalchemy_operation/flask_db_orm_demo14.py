from flask import Flask
from sqlalchemy import Column, String, Integer, ForeignKey, Enum, func
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
    name = Column(String(64), nullable=False, unique=True)
    age = Column(Integer)
    gender = Column(Enum('female', 'male', 'secret'), default='male')

    def __repr__(self):
        return '<User {}>'.format(self.name)


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# u1 = User(name='张三', age=18, gender='male')
# u2 = User(name='李四', age=18, gender='male')
# u3 = User(name='王五', age=20, gender='female')
# u4 = User(name='马六', age=21, gender='male')
# u5 = User(name='柳七', age=22, gender='female')
#
# session.add_all([u1, u2, u3, u4, u5])
# session.commit()

# users = session.query(User.age, func.count(User.id)).group_by(User.age).all()
# print(users)

users = session.query(User.gender, func.count(User.id)).group_by(User.gender).all()
print(users)