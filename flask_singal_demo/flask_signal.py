from flask import Flask, request, g, template_rendered, render_template, got_request_exception
from signals import login_signal2

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


def template_rendered_func(sender, template, context):
    print(sender)
    print(template)
    print(context)
template_rendered.connect(template_rendered_func)


def got_request_exception_func(sender, *args, **kwargs):
    print(sender)
    print(args)
    print(kwargs)

got_request_exception.connect(got_request_exception)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    username = request.args.get('username')
    if username:
        g.user = username
        login_signal2.send()
        return '登录成功'
    else:
        return '请输入用户名'


if __name__ == '__main__':
    app.run()