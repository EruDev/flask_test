import enum
from datetime import datetime
from flask import Flask
from sqlalchemy import Column, Integer, String, create_engine, DateTime, Boolean, DECIMAL, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


USER = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
DB = 'flask_sqlalchemy01'
PORT = 3306


# mysql+pymysql://root:root@127.0.0.1:3306/flask_sqlalchemy01?charset=utf8
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'\
                            .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)


app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})

@app.route('/')
def index():
    return 'hello world'


class TagEnum(enum.Enum):
    python = 'Python'
    django = 'DJANGO'
    flask = 'Flask'


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # name = Column(String(64))
    # date = Column(DateTime, default=datetime.now())
    # is_delete = Column(Boolean())
    # price = Column(DECIMAL(10, 4))
    # tag = Column(Enum('Python', 'Flask', 'Django'))
    # tag = Column(Enum(TagEnum))
    content = Column(String(64), unique=True, nullable=True, default='测试内容', onupdate=datetime.now())

Base.metadata.drop_all()
Base.metadata.create_all()
session = sessionmaker(engine)()

article = Article()
session.add(article)
session.commit()


