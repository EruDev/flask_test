import os
from flask import Flask, request, g, url_for, session

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True,
    'SECRET_KEY' : os.urandom(6)
})


@app.route('/')
def index():
    username = request.args.get('username')
    g.username = username

    if hasattr(g, 'user'):
        print(g.user)
    return 'hello world'


@app.route('/list')
def my_list():
    session['user_id'] = 1
    return 'my list'



# @app.before_first_request
# def first():
#     print('hello python')


with app.test_request_context():
    user_id = session.get('user_id')
    if user_id:
        g.user = 'zhangsan'
    print(url_for('my_list'))


if __name__ == '__main__':
    app.run()