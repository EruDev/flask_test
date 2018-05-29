import os
from flask import Flask, Response, session

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True,
    'SECRET_KEY': os.urandom(6)
})

@app.route('/')
def hello_world():
    resp = Response()
    resp.set_cookie('session')
    session['username'] = 'zhangsan'
    return 'hello world!'


@app.route('/get_session')
def get_session():
    resp = session.get('username')
    return resp or '没有session'

@app.route('/del_session')
def del_session():
    session.pop('username')
    return '删除成功'


if __name__ == '__main__':
    app.run(debug=True)
