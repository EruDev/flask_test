from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


USER = 'root'
PASSWORD = 'your password'
DB = 'flask_sqlalchemy01'
PORT = 3306
HOST = '127.0.0.1'


# mysql+pymysql://root:root@127.0.0.1:3306/flask_sqlalchemy01?charset=utf8
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'\
                            .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)

session = sessionmaker(engine)()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    age = Column(Integer)
    country = Column(String(128))

    def __str__(self):
        return '<User {}>'.format(self.name)


Base.metadata.create_all()


# 增
def add_data():
    p1 = Person(name='zhangsan', age=18, country='beijing')
    p2 = Person(name='lisi', age=20,country='shanghai')
    session.add_all([p1, p2])
    session.commit()

# 查
def query_data():
    # all_person = session.query(Person).all()
    # print(all_person)
    # for person in all_person:
    #     print(person)
    # person = session.query(Person).filter_by(name='zhangsan').first()
    # print(person)
    person = session.query(Person).filter(Person.name == 'zhangsan').all()
    print(person)

# 改
def update_data():
    person = session.query(Person).first()
    person.name = 'laowang'
    session.commit()


# 删
def delete_data():
    person = session.query(Person).all()[0]
    print(person)
    session.delete(person)
    session.commit()


if __name__ == '__main__':
    # add_data()
    # query_data()
    # update_data()
    delete_data()