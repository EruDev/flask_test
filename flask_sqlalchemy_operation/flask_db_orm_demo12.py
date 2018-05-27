from flask import Flask
from sqlalchemy import Column, String, Integer
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=Flask)

    def __repr__(self):
        return '<Post {}>'.format(self.title)


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# for i in range(100):
#     p = Post(title='title %s' % i)
#     session.add(p)
# session.commit()

# ps = session.query(Post).offset(10).limit(10).all()
# print(ps)

# ps = session.query(Post).order_by(Post.id.desc())[:10]
# print(ps)

ps = session.query(Post)[20:30] # 切片操作
print(ps)