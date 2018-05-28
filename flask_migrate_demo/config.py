HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
DB = 'flask_script_demo'
PORT = 3306

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'.format(user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
TEMPLATES_AUTO_RELOAD = True