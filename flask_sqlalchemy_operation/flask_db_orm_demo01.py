from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


HOST = '127.0.0.1'
PORT = 3306
DB = 'flask_sqlalchemy01'
USER = 'root'
PASSWORD = 'root'

# mysql+pymysql://root:root@127.0.0.1:3306/flask_sqlalchemy01?charset=utf8
DB_URI = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8"\
            .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)

engine = create_engine(DB_URI)

Base = declarative_base(engine)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    age = Column(Integer)


Base.metadata.create_all() # 将模型映射到数据库