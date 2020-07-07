from flask import Blueprint, render_template, views, request, redirect, url_for, session, config

from .models import CmsUser

blue_cms = Blueprint('blue_cms',__name__,url_prefix='/cms')
from .froms import LoginForm

@blue_cms.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('cms/cms_login.html')
    else:

        return '请求方式不允许'

# request.files 上传文件
# request.args  get请求参数获取
# request.form  post请求


class LoginView(views.View):

    def get(self):
        return render_template('../templates/cms/cms_login.html')

    def post(self):
        # 实例化一个表单对象
        # 判断用户是否输入符合要求
        # 接受浏览器表单输入内容
        # 验证成功将用户信息存储到session中
        # 成功以后跳转
        form = LoginForm(request.form)
        if form.validate():# 满足限制
            email = form.email.data
            password = form.password.data
            remember = form.remember.data

            user = CmsUser.query.filter_by(email=email).first()
            print(user)
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id# 用户名密码都正确 所以将id存入session中
                if remember:
                    session.permanent = True #如果用户勾选 那么默认过期时  31天
                return redirect(url_for('blue_cms.index'))
        else:
            return redirect((url_for('blue_cms.login')))


blue_cms.add_url_rule('/login',view_func=LoginView.as_view('login'))