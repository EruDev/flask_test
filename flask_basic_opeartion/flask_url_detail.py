from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '你居然能访问到我'


if __name__ == '__main__':
    # 指定地址0.0.0.0 端口9000 这样同一局域网内的都能访问到了
    app.run(debug=True, host='0.0.0.0', port=9001)