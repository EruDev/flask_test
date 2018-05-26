from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'


@app.route('/login')
def login():
    return '这是登录页面'


@app.route('/profile')
def profile():
    if request.args.get('name'):
        name = request.args.get('name')
        return '你好: %s' % name
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)