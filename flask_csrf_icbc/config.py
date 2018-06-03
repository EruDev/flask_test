import os

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
PORT = 3306
DB = 'flask_sqlalchemy01'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'\
                            .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(64)