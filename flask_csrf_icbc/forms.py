from wtforms import Form, StringField, PasswordField, FloatField
from wtforms.validators import Email, EqualTo, Length, InputRequired, NumberRange

from models import User


class RegistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(3, 20)])
    password = PasswordField(validators=[Length(6, 10)])
    password_repeat = PasswordField(validators=[EqualTo('password')])
    deposit = FloatField(validators=[InputRequired()])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    password = PasswordField(validators=[Length(6, 10)])

    # def validate(self):
    #     result = super(LoginForm, self).validate()
    #     email = self.email.data
    #     password = self.password.data
    #     user = User.query.filter(User.email == email, User.password == password).first()
    #     if not user:
    #         self.email.errors.append('邮箱或密码错误!')
    #         return False
    #     return True


class TransferForm(Form):
    email = StringField(validators=[Email()])
    money = FloatField(validators=[NumberRange(1, 1000000)])
