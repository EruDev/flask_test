from flask import Flask, views, jsonify, render_template

app = Flask(__name__)


class JsonView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data()) # 返回的是一个 json 对象 response


class ListView(JsonView):
    def get_data(self):
        return {'username': 'zhangsan', 'age': 18, 'addr': '北京'}

app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD': True
})
# 如果使用了类视图, as_view('指定视图名'). 指定了 endpoint 那么在浏览器中调 url时, 就需要使用这个值
app.add_url_rule('/list/', endpoint='list', view_func=ListView.as_view('list'))


class ADSView(views.View):
    def __init__(self):
        super(ADSView, self).__init__()
        self.context = {
            'ads': 'Python大法好啊'
        }


class LoginView(ADSView):
    def dispatch_request(self):
        return render_template('login.html', **self.context)


class RegisView(ADSView):
    def dispatch_request(self):
        self.context.update({
            'pic': '这是一幅画, 你看不见而已'
        })
        return render_template('register.html', **self.context)

app.add_url_rule('/login', view_func=LoginView.as_view('login'))
app.add_url_rule('/register', view_func=RegisView.as_view('register'))


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()