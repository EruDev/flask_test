from flask import Flask, views, jsonify, render_template

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


class ListView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data()) # 返回 json 对象 直接是一个response


class JSONView(ListView):
    def get_data(self):
        return {'user': '张三', 'age': 18, 'addr': '北京', 'tel': '429564909'}

app.add_url_rule('/list/', endpoint='list', view_func=JSONView.as_view('list'))


class ADSView(views.View):
    def __init__(self):
        super(ADSView, self).__init__()
        self.context = {
            'ads': 'Python 大法好啊',
            'gz': '这是一则广告',
        }

class LoginView(ADSView):
    def dispatch_request(self):
        self.context.update({
            'login': '登录页面'
        })
        return render_template('login.html', **self.context)


class RegisterView(ADSView):
    def dispatch_request(self):
        self.context.update({
            'register': '注册页面',
        })
        return render_template('register.html', **self.context)

app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/register/', view_func=RegisterView.as_view('register'))


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()