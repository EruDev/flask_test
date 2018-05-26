from flask import Flask, request, views
from functools import wraps

app = Flask(__name__)

app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


def login_requried(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        if username and username == 'zhangsan':
            return '登录成功'
        else:
            return '请先登录'
    return wrapper


class ProfileView(views.View):
    decorators = [login_requried]
    def dispatch_request(self):
        return '这是个人资料界面'


app.add_url_rule('/profile', view_func=ProfileView.as_view('profile'))


@app.route('/')
@login_requried
def index():
    return 'hello world'


@app.route('/settings/')
@login_requried
def settings():
    return '这是设置页面'


if __name__ == '__main__':
    app.run()