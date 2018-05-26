from flask import Flask, views, request, render_template, flash

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


class LoginMethView(views.MethodView):

    def __render(self, error=None):
        return render_template('login.html', error=error)

    def get(self):
        return self.__render()

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhangsan' and password == '111':
            return '登录成功'
        else:
            return self.__render(error='用户名或密码错误')

app.add_url_rule('/login/', view_func=LoginMethView.as_view('login'))


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()