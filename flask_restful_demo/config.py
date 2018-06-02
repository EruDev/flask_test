HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWORD = 'root'
DB = 'flask_Sqlalchemy01'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'\
                    .format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False