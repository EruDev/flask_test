from flask import Flask, request, render_template, redirect, url_for
from forms import RegisterForm, LoginForm, LoggingForm

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATE_AUTO_RELOAD': True,
})




@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            # print(form.errors)
            return redirect(url_for('hello_world'))
        else:
            print(form.errors)
            return 'fail'
        # username = request.form.get('username')
        # password = request.form.get('password')
        # password_repeat = request.form.get('password_repeat')
        #
        # if len(username) < 6:
        #     return '用户名不能小于6位'
        # if len(password) < 6 or len(password):
        #     return '密码不能小于6位或者大于10位'
        # if password != password_repeat:
        #     return '两次输入的密码不一致'
        # return redirect(url_for('hello_world'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'


@app.route('/logging', methods=['GET', 'POST'])
def logging():
    if request.method == 'GET':
        form = LoggingForm()
        return render_template('logging.html', form=form)
    else:
        form = LoggingForm(request.form)
        pass


if __name__ == '__main__':
    # from uuid import uuid4
    # print(uuid4())
    app.run()

