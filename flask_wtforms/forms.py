from flask_wtf.file import FileRequired, FileAllowed
from wtforms import Form, StringField, PasswordField, IntegerField, SelectField, BooleanField, FileField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, URL, UUID, Regexp


class RegisterForm(Form):
    # 这里的字段名必须和表单中定义的字段名一样
    username = StringField(validators=[Length(min=3, max=10, message='用户名必须为3-10位之间')])
    password = StringField(validators=[Length(min=6, max=10, message='密码必须要为6-10')])
    password_repeat = StringField(validators=[Length(min=6, max=10, message='密码必须要为6-10'), EqualTo('password')])


class LoginForm(Form):
    # email = StringField(label='邮箱', validators=[Email(message='邮箱输入有误')])
    # username = StringField(label='用户名', validators=[InputRequired()])
    # age = IntegerField(label='年龄', validators=[NumberRange(min=18, max=30)])
    # phone = StringField(label='手机号', validators=[Regexp(r'1[35687]\d{9}', message='手机号输入有误')])
    # home_page = StringField(label='个人主页', validators=[URL()])
    # uuid = StringField(label='uuid', validators=[UUID()])
    captcha = StringField(label='验证码', validators=[Length(4, 4)])

    def validate_captcha(self, field):
        if field.data != '1111':
            return '验证码错误'


class LoggingForm(Form):
    username = StringField(label='用户名', validators=[InputRequired()])
    age = IntegerField(label='年龄', validators=[Length(18, 35)])
    remember = BooleanField(label='记住我')
    tags = SelectField(label='标签', choices=[('1', '北京'), ('2', '上海')])


class UploadForm(Form):
    avatar = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])
    desc = StringField(label='描述', validators=[InputRequired()])