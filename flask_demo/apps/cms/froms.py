from wtforms import  StringField,IntegerField
from wtforms import Form
from wtforms.validators import Email, InputRequired, Length


class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱类型'),InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6,30,message='请输入正确长度的密码')])
    remember = IntegerField