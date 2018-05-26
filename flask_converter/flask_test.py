from flask import Flask, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)
# app.debug = True

# 自定义手机号码匹配转换器
class TelePhoneConverter(BaseConverter):
    regex = r'1[3568]\d{9}'

# 自定义list转换器, 例如用户在url中输入的是 /posts/a+b, 要求返回 a 和 b
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

app.url_map.converters['tel'] = TelePhoneConverter
app.url_map.converters['list'] = ListConverter


@app.route('/')
def index():
    print(url_for('posts', boards=['a', 'b']))
    return 'hello world'


@app.route('/login')
def login():
    return 'login'


@app.route('/phone/<tel:my_tel>')
def phone(my_tel):
    return 'my phone: %s' % my_tel


@app.route('/posts/<list:boards>')
def posts(boards):
    return '您输入的版块是: %s' % boards


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
