from flask import Flask, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.debug = True

class TelPhoneConverter(BaseConverter):
    """匹配手机号码"""
    regex = r'1[3568]\d{9}'


class ListConverter(BaseConverter):
    def to_python(self, value):
        """
        用于处理 url 后面的参数
        这个方法的返回值, 将会传递到 view 函数作为参数
        :param value:
        :return:
        """
        print(value)
        return value.split('+')

    def to_url(self, value):
        """
        这个方法的返回值, 将会调用 url_for 函数的时候生成符合要求的 URL 形式
        :param value: 这里的value 值得就是 index视图中 url_for 中的参数 boards 的值
        :return:
        """
        print(value)
        return '+'.join(value)


app.url_map.converters['tel'] = TelPhoneConverter
app.url_map.converters['list'] = ListConverter

@app.route('/')
def index():
    print(url_for('posts', boards=['吃鸡', '炉石']))
    return 'hello world'


@app.route('/login')
def login():
    return redirect(url_for('index', next='/'))


@app.route('/phone/<tel:phone_num>')
def phone(phone_num):
    return 'my phone number: %s' % phone_num


@app.route('/posts/<list:boards>')
def posts(boards):
    # print(url_for(''))
    return '您访问的版块是: %s' % boards

if __name__ == '__main__':
    app.run()