from flask import Flask, render_template, url_for
from flask_restful import Api, Resource, reqparse, inputs

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})
# 用api绑定app
api = Api(app)


class LoginView(Resource):
    def post(self, username):
        parser = reqparse.RequestParser()
        # parser.add_argument('username', type=str, help='用户名错误')
        # parser.add_argument('password', type=str, help='密码错误')
        # parser.add_argument('home_page', type=inputs.url, help='个人主页地址错误')
        # parser.add_argument('tel', type=inputs.regex(r'1[35687]\d{9}'), help='手机号错误')
        # parser.add_argument('birthday', type=inputs.date, help='生日验证错误')
        parser.add_argument('gender', type=str, choices=('male', 'female', 'secret'), help='输入的性别有误')
        args = parser.parse_args() # 解析参数
        print(args)
        return {'username': 'zhangsan'}

api.add_resource(LoginView, '/login/<username>', endpoint='login') # endpoint 用于url_for反转的时候

with app.test_request_context():
    print(url_for('login', username='maliu'))


@app.route('/')
def hello_world():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
