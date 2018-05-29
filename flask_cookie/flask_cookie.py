from datetime import datetime
from flask import Flask, request, Response

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


@app.route('/')
def hello_world():
    expires = datetime(year=2018, month=5, day=30, hour=0, minute=0, second=0)
    response = Response('hello world')
    response.set_cookie('username', 'zhangsan', expires=expires) # max_age=60
    return response


@app.route('/del')
def delete_cookie():
    response = Response('删除cookie')
    response.delete_cookie('username')
    return response


if __name__ == '__main__':
    app.run()
