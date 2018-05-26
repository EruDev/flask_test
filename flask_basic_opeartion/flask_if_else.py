from flask import Flask, render_template

app = Flask(__name__)
app.config.update({
    'DEBUG': True, # 开启 debug 模式
    'TEMPLATES_AUTO_RELOAD':True # 不用手动重启 127.0.0.1
})

@app.route('/')
def index():
    context = {
        'username': 'zhangsan',
        'age': 19
    }
    return render_template('if_else.html', **context)


if __name__ == '__main__':
    app.run()