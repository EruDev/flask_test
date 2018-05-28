from flask import Flask
from sqlalchemy import Column, String, Integer, ForeignKey, Table
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
    'TEMPLATES_AUTO_RELOAD': True
})

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'.format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = sessionmaker(engine)()
Base = declarative_base(engine)


@app.route('/')
def index():
    return 'hello world'

"""
定义多对多关系
"""
post_tag = Table(
    "post_tag", # 表名
    Base.metadata,
    Column('post_id', Integer, ForeignKey('post.id'), primary_key=True), # 绑定 post_id
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True), # 绑定 tag_id
)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)

    tags = relationship('Tag', backref='posts', secondary=post_tag)

    def __repr__(self):
        return '<Post {}>'.format(self.title)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))

    def __repr__(self):
        return '<Tag {}>'.format(self.name)

Base.metadata.drop_all()
Base.metadata.create_all()

p1 = Post(title='post01')
p2 = Post(title='post02')

t1 = Tag(name='tag01')
t2 = Tag(name='tag02')

p1.tags.append(t1)
p1.tags.append(t2)

p2.tags.append(t1)
p2.tags.append(t2)

session.add_all([p1, p2])
session.commit()

