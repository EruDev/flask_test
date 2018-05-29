from flask import Flask, render_template, request

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


@app.route('/')
def index():
    return 'hello world'


@app.route('/register', methods=['GET', 'POST'])
def register():
    # if request.method == 'GET':
    #     return render_template('books.html')
    # else:
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     password_repeat = request.form.get('password_repeat')
    #
    #     if len(username) < 6:
    #         return '用户名不能小于 6 位'
    #     if len(password) < 6 or len(password) > 10:
    #         return '密码不能小于 6 位或者大于 10 位'
    #     if password != password_repeat:
    #         return  '两次输入的密码不一致'
    return render_template('login.html')
    # return 'register'

if __name__ == '__main__':
    app.run()