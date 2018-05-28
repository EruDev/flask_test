# """
# flask-script 练习
# """
# from flask_script import Manager
# from models import app
#
# manager = Manager(app)
#
#
#
#
# @manager.option('-n', '--name', dest='name')
# @manager.option('-a', '--age', dest='age')
# def add_user(name, age):
#     print('输入的用户名: %s, 年龄: %s' % (name, age))
#
# if __name__ == '__main__':
#     manager.run()

from flask_script import Manager
from .models import app, db, BackendUser


manager = Manager(app)


@manager.option('-u', '--username', dest='username')
@manager.option('-e', '--email', dest='email')
def add_user(username, email):
    u = BackendUser(username=username, email=email)
    db.session.add(u)
    db.session.commit()


if __name__ == '__main__':
    manager.run()